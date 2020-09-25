# -*- coding: utf-8 -*-
import numpy as np
from base_validation_case import BaseValidationCase

class SetupValidationCase07(BaseValidationCase):
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
            "Vair": 52.5, 
            "rhoair": 1.19, 
            "cair": 0,
            "splitfac": 0.09,
            "g": 1,
            "alphaiwi": 2.24,
            "alphaowi": 2.7,
            "alphaWall": 25 * 10.5, # 25 * sum(Ao)
            "withInnerwalls": True
        }
    
    def get_internal_gains_radiative(self):
        return self._get_profile(0, 1000, 6, 18)
    
    def get_set_temperature_heating(self):
        return self._get_profile(22, 27, 6, 18) + 273.15
    
    def get_set_temperature_cooling(self):
        return self.get_set_temperature_heating()
    
    def get_maximum_heater_output(self):
        power_limit = np.zeros((self.total_timesteps, 3))
        power_limit[:,0] = 500
        return power_limit
    
    def get_maximum_chiller_output(self):
        return -self.get_maximum_heater_output()
