#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 02 12:52:24 2016

@author: tsz
"""
from __future__ import division

import numpy as np

def equal_air_temp(HSol, TBlaSky, TDryBul, sunblind, params):
    """
    Computes the equivalent air temperature on exterior walls without considering windows seperately
    (several approaches possible here)
    
    Arguments
    ---------
    HSol: numpy ndarray 
           solar radiation per unit area
    TBlaSky: numpy ndarray
             black-body sky temperature
    TDryBul: numpy ndarray
             dry bulb temperature
    sunblind: numpy ndarray
              opening factor of sunblinds for each direction (0 = open to 1 = closed, sunblinds.sunblindsig)
    params: dictionary
            misc. constant input parameters
            - eExt: float
                    coefficient of emission of exterior walls (outdoor)
            - aExt: float
                    coefficient of absorption of exterior walls (outdoor)
            - alpha_rad_wall: int/float
                              heat transfer coefficient
            - alpha_wall_out: int/float
                              heat transfer coefficient
            - wfWall: float
                      weight factors of the walls
            - wfWin: float
                     weight factors of the windows
            - wfGro: float
                     weight factor of the ground (0 if not considered)
            - T_Gro: int/float
                     constant ground temperature
            - withLongwave: boolean
                            True if longwave radiation is considered

    Returns
    -------
    TEqAir: numpy ndarray
            equivalent air temperature on exterior walls for convective heat entry
    """
    # Read parameters to improve readability in the equations
    eExt = params["eExt"]
    aExt = params["aExt"]
    alphaRadWall = params["alpha_rad_wall"]
    alphaWallOut = params["alpha_wall_out"]
    wfWall = params["wfWall"]
    wfWin = params["wfWin"]
    wfGro = params["wfGro"]
    TGro = params["T_Gro"]
    n = len(wfWall)
    
    # Compute equivalent long wave and short wave temperatures
    delTEqLW = (TBlaSky - TDryBul) * (eExt * alphaRadWall / (alphaRadWall + alphaWallOut * 0.93))
    delTEqSW = HSol * aExt / (alphaRadWall + alphaWallOut)
    
    # Compute equivalent window and wall temperatures
    if params["withLongwave"]:
        TEqWin = np.array([TDryBul + delTEqLW * (1 - sunblind[:,i]) for i in range(n)]).T
        TEqWall = np.array([TDryBul + delTEqLW[:,i] + delTEqSW[:,i] for i in range(n)]).T
    else:
        TEqWin = np.array([TDryBul for i in range(n)]).T
        TEqWall = np.array([TDryBul + delTEqSW[:,i] for i in range(n)]).T
    
    # Compute equivalent air temperature
    TEqAir = np.dot(TEqWall, wfWall) + np.dot(TEqWin, wfWin) + TGro * wfGro
    
    # Return result
    return TEqAir
