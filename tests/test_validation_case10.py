#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setup_validation_case_10 import SetupValidationCase10
from test_case_executor import run_validation_case
from evaluation import TemperatureTestEvaluation

class TestCase10:
    def test_case_10(self):
        case = SetupValidationCase10()
        
        temperature_air_mean, _, _ = run_validation_case(case)
        
        evaluator = TemperatureTestEvaluation("inputs/case10_res.csv", 0.13)
        evaluator.evaluate_results(temperature_air_mean)
