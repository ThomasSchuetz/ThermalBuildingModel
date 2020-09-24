# -*- coding: utf-8 -*-
import numpy as np
from base_validation_case import BaseValidationCase

class SetupValidationCase11(BaseValidationCase):
    def __init__(self, times_per_hour=60, total_days=60):
        super().__init__(times_per_hour, total_days)
    
    def get_building_parameters(self):
        return {
            "R1i": 0.000595693407511, 
            "C1i": 14836354.6282, 
            "Ai": 75.5, 
            "RRest": 0.03895919557, 
            "R1o": 0.00436791293674, 
            "C1o": 1600848.94,
            "Ao": [10.5], 
            "Aw": np.zeros(1), 
            "At": [0], 
            "Vair": 0, 
            "rhoair": 1.19, 
            "cair": 1007,
            "splitfac": 0.09,
            "g": 1,
            "alphaiwi": 3,
            "alphaowi": 2.7,
            "alphaWall": 25 * 10.5, # 25 * sum(Ao)
            "withInnerwalls": True
        }
    
    def get_internal_gains_radiative(self):
        source_igRad = np.zeros(self.timesteps_day)
        for q in range(int(6 * self.timesteps_day / 24), 
                       int(18 * self.timesteps_day / 24)):
            source_igRad[q] = 1000
        
        return np.tile(source_igRad, 60)
    
    def get_set_temperature_heating(self):
        t_set = np.zeros(self.timesteps_day) + 273.15 + 22
        for q in range(int(6 * self.timesteps_day / 24), 
                       int(18 * self.timesteps_day / 24)):
            t_set[q] = 273.15 + 27
        
        return np.tile(t_set, 60)
    
    def get_set_temperature_cooling(self):
        return self.get_set_temperature_heating()
    
    def get_maximum_heater_output(self):
        power_limit = np.zeros((self.total_timesteps, 3))
        power_limit[:,0] = 500
        return power_limit
    
    def get_maximum_chiller_output(self):
        power_limit = np.zeros((self.total_timesteps, 3))
        power_limit[:,1] = -500
        return power_limit
    
    def get_chiller_order(self):
        return np.array([2,1,3])
