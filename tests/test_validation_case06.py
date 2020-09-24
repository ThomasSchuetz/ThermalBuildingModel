#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setup_validation_case_06 import SetupValidationCase06
from test_case_executor import run_validation_case
from evaluation import PowerTestEvaluation

class TestCase06:
    def test_case_06(self):
        case = SetupValidationCase06()
        
        _, Q_hc_mean, _ = run_validation_case(case)
        
        evaluator = PowerTestEvaluation("inputs/case06_res.csv", 1.2)
        evaluator.evaluate_results(-Q_hc_mean) # Different sign convention --> flip sign
