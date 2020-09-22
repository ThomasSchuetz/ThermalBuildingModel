#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 09 16:37:05 2016

@author: tsz
"""
import numpy as np
from thermal_building_model.low_order_VDI import reducedOrderModelVDI
import tcParams as tc

class TestCase01:
    def test_case_01(self):
        # Definition of time horizon
        times_per_hour = 60
        timesteps = 24 * 60 * times_per_hour # 60 days
        timesteps_day = int(24 * times_per_hour)
        
        # Zero inputs    
        ventRate = np.zeros(timesteps)
        solarRad_in = np.zeros((timesteps,1))
        source_igRad = np.zeros(timesteps)
        
        # Constant inputs
        alphaRad = np.zeros(timesteps) + 5
        equalAirTemp = np.zeros(timesteps) + 295.15 # all temperatures in K
        weatherTemperature = np.zeros(timesteps) + 295.15 # in K
        
        # Variable inputs
        Q_ig = np.zeros(timesteps_day)
        for q in range(int(6*timesteps_day/24), int(18*timesteps_day/24)):
            Q_ig[q] = 1000
        Q_ig = np.tile(Q_ig, 60)
        
        # Load constant house parameters
        houseData = tc.get_house_data(case=1)
        
        krad = 1
        
        # Define set points (prevent heating or cooling!)
        t_set_heating = np.zeros(timesteps)        # in Kelvin
        t_set_cooling = np.zeros(timesteps) + 600  # in Kelvin
        
        heater_limit = np.zeros((timesteps,3)) + 1e10
        cooler_limit = np.zeros((timesteps,3)) - 1e10
        
        # Calculate indoor air temperature
        T_air, Q_hc, Q_iw, Q_ow = reducedOrderModelVDI(houseData, weatherTemperature, solarRad_in,
                                           equalAirTemp, alphaRad, ventRate, Q_ig, source_igRad, krad,
                                           t_set_heating, t_set_cooling, heater_limit, cooler_limit,
                                           heater_order=np.array([1,2,3]), cooler_order=np.array([1,2,3]),
                                           dt=int(3600/times_per_hour))
        
        # Compute averaged results
        T_air_c = T_air - 273.15
        T_air_mean = np.array([np.mean(T_air_c[i*times_per_hour:(i+1)*times_per_hour]) for i in range(24*60)])
        
        T_air_1 = T_air_mean[0:24]
        T_air_10 = T_air_mean[216:240]
        T_air_60 = T_air_mean[1416:1440]
        
        # Load reference results    
        (T_air_ref_1, T_air_ref_10, T_air_ref_60) = tc.load_res("inputs/case01_res.csv")
        T_air_ref_1 = T_air_ref_1[:,0]
        T_air_ref_10 = T_air_ref_10[:,0]
        T_air_ref_60 = T_air_ref_60[:,0]
        
        max_deviation_day_1 = np.max(np.abs(T_air_1 - T_air_ref_1))
        max_deviation_day_10 = np.max(np.abs(T_air_10 - T_air_ref_10))
        max_deviation_day_60 = np.max(np.abs(T_air_60 - T_air_ref_60))
        
        if max_deviation_day_1 > 0.1:
            raise "Deviation on day 1 exceeds 0.1 K" + str(max_deviation_day_1)
        if max_deviation_day_10 > 0.1:
            raise "Deviation on day 1 exceeds 0.1 K" + str(max_deviation_day_10)
        if max_deviation_day_60 > 0.1:
            raise "Deviation on day 1 exceeds 0.1 K" + str(max_deviation_day_60)