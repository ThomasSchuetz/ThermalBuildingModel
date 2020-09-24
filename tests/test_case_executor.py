# -*- coding: utf-8 -*-
import numpy as np
from thermal_building_model.low_order_VDI import reducedOrderModelVDI

def run_validation_case(setup_object):
    """
    This function shall use a setup_validation_case object to run a test case and 
    return hourly averaged temperature and heating power series
    """
    T_air, Q_hc, Q_iw, Q_ow = reducedOrderModelVDI(
        setup_object.get_building_parameters(), 
        setup_object.get_weather_temperature(), 
        setup_object.get_solar_radiation(),
        setup_object.get_equal_air_temperature(), 
        setup_object.get_alpha_radiative(), 
        setup_object.get_ventilation_rate(), 
        setup_object.get_internal_gains_convective(), 
        setup_object.get_internal_gains_radiative(), 
        setup_object.get_k_radiative(),
        setup_object.get_set_temperature_heating(), 
        setup_object.get_set_temperature_cooling(), 
        setup_object.get_maximum_heater_output(), 
        setup_object.get_maximum_chiller_output(),
        setup_object.get_heater_order(), 
        setup_object.get_chiller_order(), 
        setup_object.get_time_discretization()
    )

    T_air_celsius = T_air - 273.15
    Q_total = Q_hc + Q_iw + Q_ow
    
    times_per_hours = setup_object.times_per_hour
    total_hours = setup_object.total_hours
    
    return (
        _get_hourly_results(T_air_celsius, times_per_hours, total_hours),
        _get_hourly_results(Q_hc, times_per_hours, total_hours),
        _get_hourly_results(Q_total, times_per_hours, total_hours)
    )
    

def _get_hourly_results(array, times_per_hour, total_hours):
    return np.array([np.mean(array[i * times_per_hour : (i+1) * times_per_hour]) for i in range(total_hours)])