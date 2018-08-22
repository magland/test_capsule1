#!/bin/bash

# check to see if all required arguments were provided
if [ $# -eq 10 ]; then
    # assign the provided arguments to variables
    t0=${1}
    s0=${2}
    vp=${3}
    vr=${4}
    tau=${5}
    vp_rod=${6}
    vr_rod=${7}
    delta_rod=${8}
    tau_rod=${9}
    xi_rod=${10}
else
    # assign the default values to variables
    t0=0.015
    s0=0.01
    vp=50
    vr=50
    tau=0
    vp_rod=50
    vr_rod=50
    delta_rod=0.030
    tau_rod=0
    xi_rod=0.5 
fi

echo "Running main.py with arguments $t0, $s0, $vp, $vr, $tau, $vp_rod, $vr_rod, $delta_rod, $tau_rod, $xi_rod"


python -u main.py  $t0 $s0 $vp $vr $tau $vp_rod $vr_rod $delta_rod $tau_rod $xi_rod
