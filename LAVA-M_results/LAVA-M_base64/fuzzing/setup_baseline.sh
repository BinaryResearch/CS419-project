#!/bin/bash


cd baseline
mkdir baseline_0{0..4}
mkdir baseline_0{0..4}/afl_in
mkdir baseline_0{0..4}/afl_out


xargs -n 1 cp -v ../../LAVA-M_base64 <<< "baseline_00 baseline_01 baseline_02 baseline_03 baseline_04"
xargs -n 1 cp -v ../../LAVA-M_base64_mutation_seed.txt <<< "baseline_00/afl_in baseline_01/afl_in baseline_02/afl_in baseline_03/afl_in baseline_04/afl_in"
