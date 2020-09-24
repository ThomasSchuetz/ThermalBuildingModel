#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setup_validation_case_09 import SetupValidationCase09
from test_case_executor import run_validation_case
from evaluation import TemperatureTestEvaluation

class TestCase08:
    def test_case_08(self):
        case = SetupValidationCase09()
        
        temperature_air_mean, _, _ = run_validation_case(case)        
        
        evaluator = TemperatureTestEvaluation("inputs/case09_res.csv", 0.12)
        evaluator.evaluate_results(temperature_air_mean)
