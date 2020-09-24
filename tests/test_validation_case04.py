#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setup_validation_case_04 import SetupValidationCase04
from test_case_executor import run_validation_case
from evaluation import TemperatureTestEvaluation

class TestCase04:
    def test_case_04(self):
        case = SetupValidationCase04()
        
        temperature_air_mean, _, _ = run_validation_case(case)
        
        evaluator = TemperatureTestEvaluation("inputs/case04_res.csv")
        evaluator.evaluate_results(temperature_air_mean)
