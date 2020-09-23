# -*- coding: utf-8 -*-
import numpy as np
import pytest
from thermal_building_model.eqAirTemp import equal_air_temp

class TestEqualAirTemperature:
    def test_equal_air_temperature_case_08(self):
        t_outside_raw = np.loadtxt("inputs/case08_t_amb.csv", delimiter=",")
        t_outside = np.array([t_outside_raw[2*i,1] for i in range(24)])
        
        q_sol_rad_win_raw = np.loadtxt("inputs/case08_q_sol_win.csv", usecols=(1,2))
        solarRad_win = q_sol_rad_win_raw[0:24,:]
        
        sunblind_in = np.zeros_like(solarRad_win)
        sunblind_in[solarRad_win > 100] = 0.85
        
        q_sol_rad_wall_raw = np.loadtxt("inputs/case08_q_sol_wall.csv", usecols=(1,2))
        solarRad_wall = q_sol_rad_wall_raw[0:24,:]
        
        t_black_sky = np.zeros_like(t_outside) + 273.15
        
        params = {"aExt": 0.7,
                  "eExt": 0.9,
                  "wfWall": [0.05796831135677373, 0.13249899738691134],
                  "wfWin": [0.4047663456281575, 0.4047663456281575],
                  "wfGro": 0,
                  "T_Gro": 273.15+12,
                  "alpha_wall_out": 20,
                  "alpha_rad_wall": 5,
                  "withLongwave": False}
        
        t_equal_air = equal_air_temp(solarRad_wall, t_black_sky, t_outside, sunblind_in, params)
        
        expected_t_equal_air = [
            291.95, 290.25, 289.65, 289.25, 289.77, 291.24, 293.88, 296.64,
            298.94, 301.10, 302.68, 303.68, 305.13, 306.38, 307.16, 307.20,
            306.57, 305.10, 302.75, 300.15, 297.85, 296.05, 295.05, 294.05
        ]
        
        for result, expected_result in zip(t_equal_air, expected_t_equal_air):
            assert result == pytest.approx(expected_result, 0.01), (
                    f"Expected {expected_result} but actual result is {result}")
