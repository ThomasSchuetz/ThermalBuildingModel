# -*- coding: utf-8 -*-
import numpy as np
from base_validation_case import BaseValidationCase
from common_test_case_parameters import building_data_cases_01_02

class SetupValidationCase01(BaseValidationCase):
    def __init__(self, times_per_hour=60, total_days=60):
        super().__init__(times_per_hour, total_days)
    
    def get_building_parameters(self):
        return building_data_cases_01_02
    
    def get_internal_gains_convective(self):
        Q_ig = np.zeros(self.timesteps_day)
        for q in range(int(6 * self.timesteps_day / 24), 
                       int(18 * self.timesteps_day / 24)):
            Q_ig[q] = 1000
        
        return np.tile(Q_ig, 60)
