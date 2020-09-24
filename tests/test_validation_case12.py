#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setup_validation_case_12 import SetupValidationCase12
from test_case_executor import run_validation_case
from evaluation import TemperatureTestEvaluation

class TestCase12:
    def test_case_12(self):
        case = SetupValidationCase12()
        
        temperature_air_mean, _, _ = run_validation_case(case)        
        
        evaluator = TemperatureTestEvaluation("inputs/case12_res.csv")
        evaluator.evaluate_results(temperature_air_mean)
