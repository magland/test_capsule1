import os.path
import sys

import matplotlib.pyplot as plt
from numpy import linspace
from math import e
from scipy.stats import norm

# SOA range for the demonstration in seconds.
# Change if you want to see other ranges.
SOAs = linspace(-0.100,0.100, num=2000)


# Get parameters from user interface
t0 = float(sys.argv[1])  # Seconds
s0 = float(sys.argv[2])  # Seconds
vp = float(sys.argv[3])  # Hz
vr = float(sys.argv[4])  # Hz
tau = float(sys.argv[5]) # Seconds 
vp_roi = float(sys.argv[6])  # Hz
vr_roi = float(sys.argv[7])  # Hz
delta_roi = float(sys.argv[8]) # Seconds
tau_roi = float(sys.argv[9]) # Seconds 
xi_roi   = float(sys.argv[10])

# Exponential race model of stimulus encoding; used by both models. 
def P_p_1st(vp, vr, SOAs):
    return (SOAs <= 0) * (1-e**(-vp*abs(SOAs)) + e**(-vp*abs(SOAs))*(vp / float(vp+vr))) + \
           (SOAs >  0) * (e**(-vr*abs(SOAs))*(vp/float(vp+vr))) 

# TVA-reset model plateau mechanism.
def tva_reset(SOAs, vp, vr, t0, s0, tau):
    return ((SOAs + tau) <= 0) * (norm.cdf((SOAs+t0+tau) / s0)  * (vp / (vr+vp)) +\
                                (1 - norm.cdf((SOAs+t0+tau) / s0)) * P_p_1st(vp,vr, SOAs+tau)) + \
           ((SOAs + tau) > 0) * ((1- norm.cdf((SOAs-t0+tau) / s0)) * (vp / (vr+vp)) +\
                                norm.cdf((SOAs-t0+tau) / s0) * P_p_1st(vp,vr, SOAs+tau))

# Range of indecision model mechanism.
def range_of_indecision(SOAs, vp, vr, delta, tau, xi):
    pf =  P_p_1st(vp,vr, -delta+SOAs+tau) 
    rf =  1-P_p_1st(vp,vr, delta+SOAs+tau) 
    s = (1.0-xi)*(1 - pf - rf)
    return   pf+s


y_reset = tva_reset(SOAs, vp,vr, t0, s0, tau)
y_range = range_of_indecision(SOAs, vp_roi, vr_roi, delta_roi, tau_roi, xi_roi) 
plt.plot(SOAs,y_reset,'b', label = 'TVA-reset')
plt.plot(SOAs,y_range,'r', label = 'Range of indecision')
plt.axhline(y=0.5,linewidth=1)
plt.axvline(x=0,linewidth=1)
plt.legend()
plt.xlabel('SOA in seconds')
plt.ylabel('"Probe first" reports')
    

plt.savefig('../results/fig1.png')
plt.savefig('../results/fig1.svg')
