#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setup_validation_case_02 import SetupValidationCase02
from test_case_executor import run_validation_case
from evaluation import TemperatureTestEvaluation

class TestCase02:
    def test_case_02(self):
        case = SetupValidationCase02()
        
        temperature_air_mean, _, _ = run_validation_case(case)
        
        evaluator = TemperatureTestEvaluation("inputs/case02_res.csv")
        evaluator.evaluate_results(temperature_air_mean)
