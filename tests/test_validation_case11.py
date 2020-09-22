#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from thermal_building_model.low_order_VDI import reducedOrderModelVDI
import tcParams as tc
from evaluation import TemperatureTestEvaluation, PowerTestEvaluation

class TestCase11:
    def test_case_11(self):
        # Definition of time horizon
        times_per_hour = 60
        timesteps = 24 * 60 * times_per_hour # 60 days
        timesteps_day = int(24 * times_per_hour)
        
        # Zero inputs    
        ventRate = np.zeros(timesteps)
        solarRad_in = np.zeros((timesteps,1))
        Q_ig = np.zeros(timesteps)
        
        # Constant inputs
        alphaRad = np.zeros(timesteps) + 5
        equalAirTemp = np.zeros(timesteps) + 295.15 # all temperatures in K
        weatherTemperature = np.zeros(timesteps) + 295.15 # in K
        
        # Variable inputs
        source_igRad = np.zeros(timesteps_day)
        for q in range(int(6*timesteps_day/24), int(18*timesteps_day/24)):
            source_igRad[q] = 1000
        source_igRad = np.tile(source_igRad, 60)
        
        # Load constant house parameters
        houseData = tc.get_house_data(case=11)
        
        krad = 1
        
        # Define set points
        t_set = np.zeros(timesteps_day) + 273.15 + 22
        for q in range(int(6*timesteps_day/24), int(18*timesteps_day/24)):
            t_set[q] = 273.15 + 27
        t_set = np.tile(t_set, 60)
        t_set_heating = t_set
        t_set_cooling = t_set
               
        heater_limit = np.zeros((timesteps,3))
        cooler_limit = np.zeros((timesteps,3))
        heater_limit[:,0] = 500
        cooler_limit[:,1] = -500
        # Calculate indoor air temperature
        T_air, Q_hc, Q_iw, Q_ow = reducedOrderModelVDI(houseData, weatherTemperature, solarRad_in,
                                           equalAirTemp, alphaRad, ventRate, Q_ig, source_igRad, krad,
                                           t_set_heating, t_set_cooling, heater_limit, cooler_limit,
                                           heater_order=np.array([1,2,3]), cooler_order=np.array([2,1,3]),
                                           dt=int(3600/times_per_hour))
        
        # Compute averaged results
        Q_hc_mean = np.array([np.mean(Q_hc[i*times_per_hour:(i+1)*times_per_hour]) for i in range(24*60)])
        Q_iw_mean = np.array([np.mean(Q_iw[i*times_per_hour:(i+1)*times_per_hour]) for i in range(24*60)])
        Q_ow_mean = np.array([np.mean(Q_ow[i*times_per_hour:(i+1)*times_per_hour]) for i in range(24*60)])
        
        Q_result = Q_hc_mean + Q_iw_mean + Q_ow_mean
        
        heat_evaluator = PowerTestEvaluation("inputs/case11_res_heating.csv", 5.3)
        heat_evaluator.evaluate_results(Q_result)
        
        T_air_c = T_air - 273.15
        T_air_mean = np.array([np.mean(T_air_c[i*times_per_hour:(i+1)*times_per_hour]) for i in range(24*60)])
        
        temperature_evaluator = TemperatureTestEvaluation("inputs/case11_res_temperature.csv")
        temperature_evaluator.evaluate_results(T_air_mean)
