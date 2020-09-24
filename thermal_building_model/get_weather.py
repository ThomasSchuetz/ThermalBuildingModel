#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import thermal_building_model.sun as sun

def get_weather(filename, beta, gamma, albedo=0.2, timeZone=1,
                altitude=0, location=(49.5, 8.5)):
    """
    Parse weather related data from TRY file

    Arguments
    ---------
    filename: string
              name of the TRY file to be parsed (not all of the data is used)
    beta: array-like
          angles between exterior wall areas and the ground
    gamma: array-like
           orientations of the exterior wall areas (N = 0, E = 90, S = 180, W = 270)
    
    Returns
    -------
    rad_sky: numpy ndarray
             radiation coming from sky
    rad_earth: numpy ndarray
               radiation coming from ground
    temp: numpy ndarray
          air temperature
    sun_rad: numpy ndarray
             radiation on tilted surface areas for each orientation
    """    
    with open(filename, "r", encoding="ISO-8859-1") as f:
        weather_data = np.loadtxt(f.readlines(), skiprows=38, usecols=(8,13,14,16,17))
    temp = weather_data[:,0]        # temperature
    sun_dir = weather_data[:,1]     # direct sun radiation
    sun_diff = weather_data[:,2]    # diffuse sun radiation
    rad_sky = weather_data[:,3]     # irradiation from sky
    rad_earth = weather_data[:,4]   # irradiation from land surface
    
    # Sun radiation on surfaces
    sun_rad  = sun.getSolarGains(0, 3600, weather_data.shape[0],
                                 timeZone = timeZone,
                                 location = location,
                                 altitude = altitude,
                                 beta     = beta,
                                 gamma    = gamma,
                                 beam     = sun_dir,
                                 diffuse  = sun_diff,
                                 albedo   = albedo)
    
    return rad_sky, rad_earth, temp + 273.15, sun_rad

def get_betaGamma(orientationswallshorizontal, offset = 0):
    
    beta = orientationswallshorizontal        
    n = len(beta)
    
    gamma = np.array([0, 90, 180, 270]) + offset
    
    if n == 4:
        pass
    elif n == 5:
        gamma = np.append(gamma, [0])
    elif n == 6:
        # in the current Teaser data file: beta = [45, 90, 90, 45, 90, 90]
        gamma = -np.array([0, 0, 90, 0, 180, 270])
        
    return beta, gamma
