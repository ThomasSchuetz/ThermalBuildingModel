# -*- coding: utf-8 -*-
import numpy as np

class BaseValidationCase:
    def __init__(self, times_per_hour=60, total_days=60):
        self.times_per_hour = times_per_hour
        
        hours_per_day = 24
        self.total_timesteps = hours_per_day * times_per_hour * total_days
        self.total_hours = total_days * hours_per_day # used for result evaluation
        self.timesteps_day = int(hours_per_day * times_per_hour)
        
    def get_building_parameters(self):
        return {}
    
    def get_ventilation_rate(self):
        return np.zeros(self.total_timesteps)
    
    def get_solar_radiation(self):
        return np.zeros((self.total_timesteps, 1))
    
    def get_internal_gains_convective(self):
        # Q_ig 
        return np.zeros(self.total_timesteps)
    
    def get_internal_gains_radiative(self):
        #source_igRad
        return np.zeros(self.total_timesteps)
        
    def get_alpha_radiative(self):
        return np.zeros(self.total_timesteps) + 5
    
    def get_equal_air_temperature(self):
        return np.zeros(self.total_timesteps) + 295.15
    
    def get_weather_temperature(self):
        return np.zeros(self.total_timesteps) + 295.15
        
    def get_k_radiative(self):
        return 1
    
    def get_set_temperature_heating(self):
        return np.zeros(self.total_timesteps)
    
    def get_set_temperature_cooling(self):
        return np.zeros(self.total_timesteps) + 600
    
    def get_maximum_heater_output(self):
        return np.zeros((self.total_timesteps, 3)) + 1e10
    
    def get_maximum_chiller_output(self):
        return np.zeros((self.total_timesteps, 3)) - 1e10
    
    def get_heater_order(self):
        return np.array([1,2,3])
    
    def get_chiller_order(self):
        return np.array([1,2,3])
    
    def get_time_discretization(self):
        return int(3600 / self.times_per_hour)
    
    def get_initial_temperatures(self):
        return dict(T_air_init=295.15, T_iw_init=295.15, T_ow_init=295.15)
    
    
