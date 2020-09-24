#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setup_validation_case_07 import SetupValidationCase07
from test_case_executor import run_validation_case
from evaluation import PowerTestEvaluation

class TestCase07:
    def test_case_07(self):
        case = SetupValidationCase07()
        
        _, Q_hc_mean, _ = run_validation_case(case)
        
        evaluator = PowerTestEvaluation("inputs/case07_res.csv")
        evaluator.evaluate_results(Q_hc_mean)
