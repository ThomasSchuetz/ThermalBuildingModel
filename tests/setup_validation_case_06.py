# -*- coding: utf-8 -*-
import numpy as np
from base_validation_case import BaseValidationCase

class SetupValidationCase06(BaseValidationCase):
    def __init__(self, times_per_hour=60, total_days=60):
        super().__init__(times_per_hour, total_days)
    
    def get_building_parameters(self):
        return {
            "R1i": 0.000595515, 
            "C1i": 14836200, 
            "Ai": 75.5, 
            "RRest": 0.038959197, 
            "R1o": 0.004367913, 
            "C1o": 1600800,
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
