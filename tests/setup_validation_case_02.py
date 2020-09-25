# -*- coding: utf-8 -*-
from base_validation_case import BaseValidationCase
from common_test_case_parameters import building_data_cases_01_02

class SetupValidationCase02(BaseValidationCase):
    def __init__(self, times_per_hour=60, total_days=60):
        super().__init__(times_per_hour, total_days)
    
    def get_building_parameters(self):
        return building_data_cases_01_02
    
    def get_internal_gains_radiative(self):
        return self._get_profile(0, 1000, 6, 18)
