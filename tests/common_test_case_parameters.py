# -*- coding: utf-8 -*-
"""
Meaning of Parameters
---------------------
R1i: resistor of inner wall
C1i: capacity of inner wall
Ai: inner wall area
RRest: remaining Resistor between exterior wall and the ambient air
R1o: resistor of exterior wall
C1o: capacity of exterior wall
Ao: area of exterior wall for each orientation
Aw: window area for each orientation
At: solar radiation transmitting area of windows for each orientation
Vair: air volume
rhoair: air density
cair: thermal heat capacity of the air
splitfac: factor splitting convective and radiative gains from solar radiation
g: energy transmittance
alphaiwi: heat transfer coefficient from inner wall to air zone
alphaowi: heat transfer coefficient from outer wall to air zone
alphaWall: heat transfer coefficient from ambient air to outer wall
withInnerwalls: True, if inner walls are considered
"""

import numpy as np

building_data_cases_01_02 = {
        "R1i": 0.000595693407511, 
        "C1i": 14836354.6282, 
        "Ai": 75.5, 
        "RRest": 0.03895919557, 
        "R1o": 0.00436791293674, 
        "C1o": 1600848.94,
        "Ao": [10.5], 
        "Aw": np.zeros(1), 
        "At": np.zeros(1), 
        "Vair": 52.5, 
        "rhoair": 1.19, 
        "cair": 0,
        "splitfac": 0.09,
        "g": 1,
        "alphaiwi": 2.24,
        "alphaowi": 2.7,
        "alphaWall": 25 * 10.5, # 25 * sum(Ao)
        "withInnerwalls": True
}

building_data_cases_03_04 = {
        "R1i": 0.003237138, 
        "C1i": 7297100, 
        "Ai": 75.5, 
        "RRest": 0.039330865, 
        "R1o": 0.00404935160802, 
        "C1o": 47900,
        "Ao": [10.5], 
        "Aw": np.zeros(1), 
        "At": np.zeros(1), 
        "Vair": 52.5, 
        "rhoair": 1.19, 
        "cair": 0,
        "splitfac": 0.09,
        "g": 1,
        "alphaiwi": 2.24,
        "alphaowi": 2.7,
        "alphaWall": 25 * 10.5, # 25 * sum(Ao)
        "withInnerwalls": True
}

building_data_cases_05_12 = {
        "R1i": 0.000595693407511, 
        "C1i": 14836354.6282, 
        "Ai": 75.5, 
        "RRest": 0.03895919557, 
        "R1o": 0.00436791293674, 
        "C1o": 1600848.94,
        "Ao": [10.5], 
        "Aw": np.zeros(1), 
        "At": [7], 
        "Vair": 0, 
        "rhoair": 1.19, 
        "cair": 1007,
        "splitfac": 0.09,
        "g": 1,
        "alphaiwi": 2.24,
        "alphaowi": 2.7,
        "alphaWall": 25 * 10.5, # 25 * sum(Ao)
        "withInnerwalls": True
}

building_data_cases_08_09 = {
        "R1i": 0.000668895639141, 
        "C1i": 12391363.8631, 
        "Ai": 60.5, 
        "RRest": 0.01913729904, 
        "R1o": 0.0017362530106, 
        "C1o": 5259932.23,
        "Ao": [10.5,15], 
        "Aw": np.zeros(2), 
        "At": [7,7], 
        "Vair": 52.5, 
        "rhoair": 1.19, 
        "cair": 0,
        "splitfac": 0.09,
        "g": 1,
        "alphaiwi": 2.12,
        "alphaowi": 2.7,
        "alphaWall": 25 * 25.5, # 25 * sum(Ao)
        "withInnerwalls": True
}

equal_air_temperature_parameters_08_09 = {
        "aExt": 0.7,
        "eExt": 0.9,
        "wfWall": [0.05796831135677373, 0.13249899738691134],
        "wfWin": [0.4047663456281575, 0.4047663456281575],
        "wfGro": 0,
        "T_Gro": 273.15 + 12,
        "alpha_wall_out": 20,
        "alpha_rad_wall": 5,
        "withLongwave": False
}