# -*- coding: utf-8 -*-
from setup_validation_case_01 import SetupValidationCase01
from setup_validation_case_02 import SetupValidationCase02
from setup_validation_case_03 import SetupValidationCase03
from setup_validation_case_04 import SetupValidationCase04
from setup_validation_case_05 import SetupValidationCase05
from setup_validation_case_06 import SetupValidationCase06
from setup_validation_case_07 import SetupValidationCase07
from setup_validation_case_08 import SetupValidationCase08
from setup_validation_case_09 import SetupValidationCase09
from setup_validation_case_10 import SetupValidationCase10
from setup_validation_case_11 import SetupValidationCase11
from setup_validation_case_12 import SetupValidationCase12
from test_case_executor import run_validation_case
from evaluation import TemperatureTestEvaluation, PowerTestEvaluation

class TestValidationCases:
    def test_case_01(self):
        case = SetupValidationCase01()
        
        temperature_air_mean, _, _ = run_validation_case(case)
        
        evaluator = TemperatureTestEvaluation("inputs/case01_res.csv")
        evaluator.evaluate_results(temperature_air_mean)
    
    
    def test_case_02(self):
        case = SetupValidationCase02()
        
        temperature_air_mean, _, _ = run_validation_case(case)
        
        evaluator = TemperatureTestEvaluation("inputs/case02_res.csv")
        evaluator.evaluate_results(temperature_air_mean)
    
    
    def test_case_03(self):
        case = SetupValidationCase03()
        
        temperature_air_mean, _, _ = run_validation_case(case)
        
        evaluator = TemperatureTestEvaluation("inputs/case03_res.csv")
        evaluator.evaluate_results(temperature_air_mean)
    
    
    def test_case_04(self):
        case = SetupValidationCase04()
        
        temperature_air_mean, _, _ = run_validation_case(case)
        
        evaluator = TemperatureTestEvaluation("inputs/case04_res.csv")
        evaluator.evaluate_results(temperature_air_mean)
    
    
    def test_case_05(self):
        case = SetupValidationCase05()
        
        temperature_air_mean, _, _ = run_validation_case(case)
        
        evaluator = TemperatureTestEvaluation("inputs/case05_res.csv")
        evaluator.evaluate_results(temperature_air_mean)
    
    
    def test_case_06(self):
        case = SetupValidationCase06()
        
        _, Q_hc_mean, _ = run_validation_case(case)
        
        evaluator = PowerTestEvaluation("inputs/case06_res.csv", 1.2)
        evaluator.evaluate_results(-Q_hc_mean) # Different sign convention --> flip sign
    
    
    def test_case_07(self):
        case = SetupValidationCase07()
        
        _, Q_hc_mean, _ = run_validation_case(case)
        
        evaluator = PowerTestEvaluation("inputs/case07_res.csv")
        evaluator.evaluate_results(Q_hc_mean)
    
    
    def test_case_08(self):
        case = SetupValidationCase08()
        
        temperature_air_mean, _, _ = run_validation_case(case)
        
        evaluator = TemperatureTestEvaluation("inputs/case08_res.csv")
        evaluator.evaluate_results(temperature_air_mean)
    
    
    def test_case_09(self):
        case = SetupValidationCase09()
        
        temperature_air_mean, _, _ = run_validation_case(case)        
        
        evaluator = TemperatureTestEvaluation("inputs/case09_res.csv", 0.12)
        evaluator.evaluate_results(temperature_air_mean)
    
    
    def test_case_10(self):
        case = SetupValidationCase10()
        
        temperature_air_mean, _, _ = run_validation_case(case)
        
        evaluator = TemperatureTestEvaluation("inputs/case10_res.csv", 0.13)
        evaluator.evaluate_results(temperature_air_mean)
    
    
    def test_case_11(self):
        case = SetupValidationCase11()
        
        temperature_air_mean, _, total_heat = run_validation_case(case)
        
        heat_evaluator = PowerTestEvaluation("inputs/case11_res_heating.csv", 5.3)
        heat_evaluator.evaluate_results(total_heat)
        
        temperature_evaluator = TemperatureTestEvaluation("inputs/case11_res_temperature.csv")
        temperature_evaluator.evaluate_results(temperature_air_mean)
    
    
    def test_case_12(self):
        case = SetupValidationCase12()
        
        temperature_air_mean, _, _ = run_validation_case(case)        
        
        evaluator = TemperatureTestEvaluation("inputs/case12_res.csv")
        evaluator.evaluate_results(temperature_air_mean)
