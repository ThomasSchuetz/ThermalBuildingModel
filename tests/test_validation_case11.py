#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setup_validation_case_11 import SetupValidationCase11
from test_case_executor import run_validation_case
from evaluation import TemperatureTestEvaluation, PowerTestEvaluation

class TestCase11:
    def test_case_11(self):
        case = SetupValidationCase11()
        
        temperature_air_mean, _, total_heat = run_validation_case(case)
        
        heat_evaluator = PowerTestEvaluation("inputs/case11_res_heating.csv", 5.3)
        heat_evaluator.evaluate_results(total_heat)
        
        temperature_evaluator = TemperatureTestEvaluation("inputs/case11_res_temperature.csv")
        temperature_evaluator.evaluate_results(temperature_air_mean)

tc = TestCase11()
tc.test_case_11()