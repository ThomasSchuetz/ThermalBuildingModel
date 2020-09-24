# -*- coding: utf-8 -*-
import numpy as np
from base_validation_case import BaseValidationCase
from common_test_case_parameters import building_data_cases_05_12

class SetupValidationCase12(BaseValidationCase):
    def __init__(self, times_per_hour=60, total_days=60):
        super().__init__(times_per_hour, total_days)
    
    def get_building_parameters(self):
        return building_data_cases_05_12
    
    def get_internal_gains_convective(self):
        Q_ig = np.zeros(self.timesteps_day)
        for q in range(int(7 * self.timesteps_day / 24), 
                       int(17 * self.timesteps_day / 24)):
            Q_ig[q] = 200 + 80
        
        return np.tile(Q_ig, 60)
    
    def get_internal_gains_radiative(self):
        source_igRad = np.zeros(self.timesteps_day)
        for q in range(int(7 * self.timesteps_day / 24), 
                       int(17 * self.timesteps_day / 24)):
            source_igRad[q] = 80
        
        return np.tile(source_igRad, 60)
    
    def get_solar_radiation(self):
        solarRad_raw = np.loadtxt("inputs/case12_q_sol.csv", usecols=(1,))
        solarRad = solarRad_raw[0:24]
        solarRad[solarRad > 100] = solarRad[solarRad > 100] * 0.15
        solarRad_win_adj = np.repeat(solarRad, self.times_per_hour)
        
        return np.array([np.tile(solarRad_win_adj, 60)]).T
        
    def get_weather_temperature(self):
        t_outside_raw = np.loadtxt("inputs/case12_t_amb.csv", delimiter=",")
        t_outside = ([t_outside_raw[2*i,1] for i in range(24)])
        t_outside_adj = np.repeat(t_outside, self.times_per_hour)
        
        return np.tile(t_outside_adj, 60)
    
    def get_equal_air_temperature(self):
        return self.get_weather_temperature()

    def get_ventilation_rate(self):
        ventRate = np.zeros(self.timesteps_day) + 100 / 3600
        for q in range(int(7 * self.timesteps_day / 24), 
                       int(17 * self.timesteps_day / 24)):
            ventRate[q] = 50 / 3600
        return np.tile(ventRate, 60)
