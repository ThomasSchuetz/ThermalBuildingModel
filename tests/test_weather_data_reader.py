# -*- coding: utf-8 -*-
import numpy as np
from pytest import approx
from thermal_building_model.get_weather import get_betaGamma, get_weather

class TestWeatherDataReader():
    def test_get_beta_gamma_four_orientations(self):
        assert np.all([0, 90, 180, 270] == get_betaGamma([0]*4)[1])
    
    def test_get_beta_gamma_five_orientations(self):
        assert np.all([0, 90, 180, 270, 0] == get_betaGamma([0]*5)[1])
        
    def test_get_beta_gamma_six_orientations(self):
        assert np.all([0, 0, 90, 0, 180, 270] == -get_betaGamma([0]*6)[1])
        
    def test_get_weather(self):
        filename = "inputs/TRY2010_12_Jahr.dat"
        beta, gamma = get_betaGamma([45, 90, 90, 45, 90, 90])
        result = get_weather(filename, beta, gamma)
        
        assert np.all([320, 303, 287, 304, 324, 320, 255] == result[0][:7])
        assert np.all([-334, -334, -332, -335, -337, -334, -329] == result[1][:7])
        assert np.all([46.56, 75.26, 140.84, 46.56, 11.32, 11.32] == approx(result[3][:,8], 0.01))
        assert np.all([279.65, 278.35, 277.55, 277.55, 277.55, 277.25, 277.05] == approx(result[2][:7], 0.01))
