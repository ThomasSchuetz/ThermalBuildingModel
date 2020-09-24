#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setup_validation_case_01 import SetupValidationCase01
from test_case_executor import run_validation_case
from evaluation import TemperatureTestEvaluation

class TestCase01:
    def test_case_01(self):
        case = SetupValidationCase01()
        
        temperature_air_mean, _, _ = run_validation_case(case)
        
        evaluator = TemperatureTestEvaluation("inputs/case01_res.csv")
        evaluator.evaluate_results(temperature_air_mean)
