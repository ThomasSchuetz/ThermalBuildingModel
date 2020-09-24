#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setup_validation_case_08 import SetupValidationCase08
from test_case_executor import run_validation_case
from evaluation import TemperatureTestEvaluation

class TestCase08:
    def test_case_08(self):
        case = SetupValidationCase08()
        
        temperature_air_mean, _, _ = run_validation_case(case)
        
        evaluator = TemperatureTestEvaluation("inputs/case08_res.csv")
        evaluator.evaluate_results(temperature_air_mean)
