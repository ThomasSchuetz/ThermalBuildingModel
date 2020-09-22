# -*- coding: utf-8 -*-
import numpy as np

class TestEvaluation:
    def __init__(self, filename, tolerance, unit):
        self.tolerance = tolerance
        self.unit = unit
        self.load_expected_results(filename)
    
    def load_expected_results(self, filename):
         # Skip time step 0 and only read the data column
        data = np.loadtxt(filename, delimiter=",", skiprows=1, usecols=(1,))
        
        self.expected_day_1 = data[0:24]
        self.expected_day_10 = data[24:48]
        self.expected_day_60 = data[48:72]
    
    def evaluate_results(self, hourly_result_series):
        result_day_1 = hourly_result_series[0:24]
        result_day_10 = hourly_result_series[216:240]
        result_day_60 = hourly_result_series[1416:1440]     
        
        self._evaluate_result(self.expected_day_1, result_day_1, "1")
        self._evaluate_result(self.expected_day_10, result_day_10, "10")
        self._evaluate_result(self.expected_day_60, result_day_60, "60")
        
    def _evaluate_result(self, expected_results, results, day_string):
        max_deviation = np.max(np.abs(expected_results - results))

        assert max_deviation <= self.tolerance, (
                f"Deviation on day {day_string} exceeds {self.tolerance} {self.unit}: {max_deviation}")
        

class TemperatureTestEvaluation(TestEvaluation):
    def __init__(self, filename, tolerance=0.1):
        super().__init__(filename, tolerance, "K")

class PowerTestEvaluation(TestEvaluation):
    def __init__(self, filename, tolerance=1):
        super().__init__(filename, tolerance, "W")