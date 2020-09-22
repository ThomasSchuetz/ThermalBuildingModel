#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from thermal_building_model.low_order_VDI import reducedOrderModelVDI
import tcParams as tc
import thermal_building_model.eqAirTemp as eq_air_temp
from evaluation import TemperatureTestEvaluation

class TestCase10:
    def test_case_10(self):
        # Definition of time horizon
        times_per_hour = 60
        timesteps = 24 * 60 * times_per_hour # 60 days
        timesteps_day = int(24 * times_per_hour)
        
        # Zero inputs    
        ventRate = np.zeros(timesteps)
        sunblind_in = np.zeros((timesteps,1))
        solarRad_wall = np.zeros((timesteps,1))
        
        # Constant inputs
        alphaRad = np.zeros(timesteps) + 5
        t_black_sky = np.zeros(timesteps) + 273.15
        
        # Variable inputs
        Q_ig = np.zeros(timesteps_day)
        source_igRad = np.zeros(timesteps_day)
        for q in range(int(7*timesteps_day/24), int(17*timesteps_day/24)):
            Q_ig[q] = 200 + 80
            source_igRad[q] = 80
        Q_ig = np.tile(Q_ig, 60)
        source_igRad = np.tile(source_igRad, 60)
        
        q_sol_rad_win_raw = np.loadtxt("inputs/case10_q_sol.csv", usecols=(1,))
        solarRad_win = q_sol_rad_win_raw[0:24]
        solarRad_win[solarRad_win > 100] = solarRad_win[solarRad_win > 100] * 0.15
        solarRad_win_adj = np.repeat(solarRad_win, times_per_hour)
        solarRad_win_in = np.array([np.tile(solarRad_win_adj, 60)]).T
        
        t_outside_raw = np.loadtxt("inputs/case10_t_amb.csv", delimiter=",")
        t_outside = ([t_outside_raw[2*i,1] for i in range(24)])
        t_outside_adj = np.repeat(t_outside, times_per_hour)
        weatherTemperature = np.tile(t_outside_adj, 60)
        
        equalAirTemp = eq_air_temp.equal_air_temp(solarRad_wall, 
                                                  t_black_sky, 
                                                  weatherTemperature, 
                                                  sunblind_in, 
                                                  tc.get_eqAirTemp_params(case=10))
        
        # Load constant house parameters
        houseData = tc.get_house_data(case=10)
        
        krad = 1
        
        # Define set points (prevent heating or cooling!)
        t_set_heating = np.zeros(timesteps)        # in Kelvin
        t_set_cooling = np.zeros(timesteps) + 600  # in Kelvin
        
        heater_limit = np.zeros((timesteps,3)) + 1e10
        cooler_limit = np.zeros((timesteps,3)) - 1e10
        
        # Calculate indoor air temperature
        T_air, Q_hc, Q_iw, Q_ow = reducedOrderModelVDI(houseData, weatherTemperature, solarRad_win_in,
                                           equalAirTemp, alphaRad, ventRate, Q_ig, source_igRad, krad,
                                           t_set_heating, t_set_cooling, heater_limit, cooler_limit,
                                           heater_order=np.array([1,2,3]), cooler_order=np.array([1,2,3]),
                                           dt=int(3600/times_per_hour),
                                           T_air_init=273.15+17.6, T_iw_init=273.15+17.6, T_ow_init=273.15+17.6)
        
        # Compute averaged results
        T_air_c = T_air - 273.15
        T_air_mean = np.array([np.mean(T_air_c[i*times_per_hour:(i+1)*times_per_hour]) for i in range(24*60)])
        
        evaluator = TemperatureTestEvaluation("inputs/case10_res.csv", 0.13)
        evaluator.evaluate_results(T_air_mean)
