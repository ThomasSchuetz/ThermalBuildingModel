#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setup_validation_case_05 import SetupValidationCase05
from test_case_executor import run_validation_case
from evaluation import TemperatureTestEvaluation

class TestCase05:
    def test_case_05(self):
        case = SetupValidationCase05()
        
        temperature_air_mean, _, _ = run_validation_case(case)
        
        evaluator = TemperatureTestEvaluation("inputs/case05_res.csv")
        evaluator.evaluate_results(temperature_air_mean)