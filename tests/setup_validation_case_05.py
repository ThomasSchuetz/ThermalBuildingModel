# -*- coding: utf-8 -*-
import numpy as np
from base_validation_case import BaseValidationCase
from common_test_case_parameters import building_data_cases_05_12

class SetupValidationCase05(BaseValidationCase):
    def __init__(self, times_per_hour=60, total_days=60):
        super().__init__(times_per_hour, total_days)
    
    def get_building_parameters(self):
        return building_data_cases_05_12
    
    def get_internal_gains_convective(self):
        return self._get_profile(0, 280, 7, 17)
    
    def get_internal_gains_radiative(self):
        return self._get_profile(0, 80, 7, 17)

    def get_solar_radiation(self):
        solarRad_raw = np.loadtxt("inputs/case05_q_sol.csv", usecols=(1,))
        solarRad = solarRad_raw[0:24]
        solarRad[solarRad > 100] = solarRad[solarRad > 100] * 0.15
        solarRad_adj = np.repeat(solarRad, self.times_per_hour)
        
        return np.array([np.tile(solarRad_adj, 60)]).T
        
    def get_weather_temperature(self):
        t_outside_raw = np.loadtxt("inputs/case05_t_amb.csv", delimiter=",")
        t_outside = ([t_outside_raw[2 * i, 1] for i in range(24)])
        t_outside_adj = np.repeat(t_outside, self.times_per_hour)
        
        return np.tile(t_outside_adj, 60)
    
    def get_equal_air_temperature(self):
        return self.get_weather_temperature()
        
        