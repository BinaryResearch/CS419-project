#!/bin/bash


cd with_all
mkdir with_all_0{0..4}
mkdir with_all_0{0..4}/afl_in
mkdir with_all_0{0..4}/afl_out


xargs -n 1 cp -v ../../LAVA-M_md5sum <<< "with_all_00 with_all_01 with_all_02 with_all_03 with_all_04" 
xargs -n 1 cp -v ../../LAVA-M_md5sum.afl_dict <<< "with_all_00 with_all_01 with_all_02 with_all_03 with_all_04"
xargs -n 1 cp -v ../../mutated_tmin/* <<<"with_all_00/afl_in with_all_01/afl_in with_all_02/afl_in with_all_03/afl_in with_all_04/afl_in"
