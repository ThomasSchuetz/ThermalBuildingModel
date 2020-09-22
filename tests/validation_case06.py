#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 13:26:01 2016

@author: tsz
"""
from __future__ import division

import numpy as np
import matplotlib.pyplot as plt

from thermal_building_model.low_order_VDI import reducedOrderModelVDI
import tcParams as tc

# Definition of time horizon
times_per_hour = 60
timesteps = 24 * 60 * times_per_hour # 60 days
timesteps_day = int(24 * times_per_hour)

# Zero inputs    
ventRate = np.zeros(timesteps)
solarRad_in = np.zeros((timesteps,1))
Q_ig = np.zeros(timesteps)

# Constant inputs
alphaRad = np.zeros(timesteps) + 5
equalAirTemp = np.zeros(timesteps) + 295.15 # all temperatures in K
weatherTemperature = np.zeros(timesteps) + 295.15 # in K

# Variable inputs
source_igRad = np.zeros(timesteps_day)
for q in range(int(6*timesteps_day/24), int(18*timesteps_day/24)):
    source_igRad[q] = 1000
source_igRad = np.tile(source_igRad, 60)

# Load constant house parameters
houseData = tc.get_house_data(case=6)

krad = 1

# Define set points
t_set = np.zeros(timesteps_day) + 273.15 + 22
for q in range(int(6*timesteps_day/24), int(18*timesteps_day/24)):
    t_set[q] = 273.15 + 27
t_set = np.tile(t_set, 60)
t_set_heating = t_set
t_set_cooling = t_set

heater_limit = np.zeros((timesteps,3)) + 1e10
cooler_limit = np.zeros((timesteps,3)) - 1e10

# Calculate indoor air temperature
T_air, Q_hc, Q_iw, Q_ow = reducedOrderModelVDI(houseData, weatherTemperature, solarRad_in,
                                   equalAirTemp, alphaRad, ventRate, Q_ig, source_igRad, krad,
                                   t_set_heating, t_set_cooling, heater_limit, cooler_limit,
                                   heater_order=np.array([1,2,3]), cooler_order=np.array([1,2,3]),
                                   dt=int(3600/times_per_hour))

# Compute averaged results
Q_hc_mean = np.array([np.mean(Q_hc[i*times_per_hour:(i+1)*times_per_hour]) for i in range(24*60)])

Q_hc_1 = Q_hc_mean[0:24]
Q_hc_10 = Q_hc_mean[216:240]
Q_hc_60 = Q_hc_mean[1416:1440]

# Load reference results    
(Q_hc_ref_1, Q_hc_ref_10, Q_hc_ref_60) = tc.load_res("inputs/case06_res.csv")
Q_hc_ref_1 = -Q_hc_ref_1[:,0]
Q_hc_ref_10 = -Q_hc_ref_10[:,0]
Q_hc_ref_60 = -Q_hc_ref_60[:,0]


# Plot comparisons
def plot_result(res, ref, title="Results day 1"):
    plt.figure()
    ax_top = plt.subplot(211)
    plt.plot(ref, label="Reference", color="black", linestyle="--")
    plt.plot(res, label="Simulation", color="blue", linestyle="-")
    plt.legend()
    plt.ylabel("Heat load in W")
    
    plt.title(title)

    plt.subplot(212, sharex=ax_top)
    plt.plot(res-ref, label="Ref. - Sim.")
    plt.legend()
    plt.ylabel("Heat load difference in W")
    plt.xticks([4*i for i in range(7)])
    plt.xlim([1,24])
    plt.xlabel("Time in h")

plot_result(Q_hc_1, Q_hc_ref_1, "Results day 1")
plot_result(Q_hc_10, Q_hc_ref_10, "Results day 10")
plot_result(Q_hc_60, Q_hc_ref_60, "Results day 60")

print("Max. deviation day 1: " + str(np.max(np.abs(Q_hc_1 - Q_hc_ref_1))))
print("Max. deviation day 10: " + str(np.max(np.abs(Q_hc_10 - Q_hc_ref_10))))
print("Max. deviation day 60: " + str(np.max(np.abs(Q_hc_60 - Q_hc_ref_60))))