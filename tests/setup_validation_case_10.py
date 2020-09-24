# -*- coding: utf-8 -*-
import numpy as np
from base_validation_case import BaseValidationCase
import thermal_building_model.eqAirTemp as eq_air_temp

class SetupValidationCase10(BaseValidationCase):
    def __init__(self, times_per_hour=60, total_days=60):
        super().__init__(times_per_hour, total_days)
    
    def get_building_parameters(self):
        return {
            "R1i": 0.000779671554640369, 
            "C1i": 12333949.4129606, 
            "Ai": 58, 
            "RRest": 0.011638548, 
            "R1o": 0.00171957697767797, 
            "C1o": 4338751.41,
            "Ao": [28], 
            "Aw": np.zeros(1), 
            "At": [7,], 
            "Vair": 52.5, 
            "rhoair": 1.19, 
            "cair": 0,
            "splitfac": 0.09,
            "g": 1,
            "alphaiwi": 2.12,
            "alphaowi": 2.398,
            "alphaWall": 28 * 9.75, # 9.75 * sum(Ao)
            "withInnerwalls": True
        }
    
    def get_internal_gains_convective(self):
        Q_ig = np.zeros(self.timesteps_day)
        for q in range(int(7 * self.timesteps_day / 24), 
                       int(17 * self.timesteps_day / 24)):
            Q_ig[q] = 200 + 80
        
        return np.tile(Q_ig, 60)
    
    def get_internal_gains_radiative(self):
        source_igRad = np.zeros(self.timesteps_day)
        for q in range(int(7 * self.timesteps_day / 24), 
                       int(17 * self.timesteps_day / 24)):
            source_igRad[q] = 80
        
        return np.tile(source_igRad, 60)
    
    def get_solar_radiation(self):
        q_sol_rad_win_raw = np.loadtxt("inputs/case10_q_sol.csv", usecols=(1,))
        solarRad_win = q_sol_rad_win_raw[0:24]
        solarRad_win[solarRad_win > 100] = solarRad_win[solarRad_win > 100] * 0.15
        solarRad_win_adj = np.repeat(solarRad_win, self.times_per_hour)
        
        return np.array([np.tile(solarRad_win_adj, 60)]).T
        
    def get_weather_temperature(self):
        t_outside_raw = np.loadtxt("inputs/case10_t_amb.csv", delimiter=",")
        t_outside = ([t_outside_raw[2*i,1] for i in range(24)])
        t_outside_adj = np.repeat(t_outside, self.times_per_hour)
        
        return np.tile(t_outside_adj, 60)
    
    def get_equal_air_temperature(self):
        sunblind_in = np.zeros((self.total_timesteps, 1))
        solarRad_wall = np.zeros((self.total_timesteps, 1))
        t_black_sky = np.zeros(self.total_timesteps) + 273.15
        
        equal_air_parameters = {
            "aExt": 0.7,
            "eExt": 0.9,
            "wfWall": [0.04646093176283288,],
            "wfWin": [0.32441554918476245,],
            "wfGro": 0.6291235190524047,
            "T_Gro": 273.15 + 15,
            "alpha_wall_out": 20,
            "alpha_rad_wall": 5,
            "withLongwave": False
        }
        
        return eq_air_temp.equal_air_temp(solarRad_wall, 
                                          t_black_sky, 
                                          self.get_weather_temperature(), 
                                          sunblind_in, 
                                          equal_air_parameters)
    
    def get_initial_temperatures(self):
        return dict(T_air_init=273.15+17.6, T_iw_init=273.15+17.6, T_ow_init=273.15+17.6)