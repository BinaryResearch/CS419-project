#!/bin/bash


cd with_dictionary
mkdir with_dictionary_0{0..4}
mkdir with_dictionary_0{0..4}/afl_in
mkdir with_dictionary_0{0..4}/afl_out


xargs -n 1 cp -v ../../LAVA-M_md5sum <<< "with_dictionary_00 with_dictionary_01 with_dictionary_02 with_dictionary_03 with_dictionary_04" 
xargs -n 1 cp -v ../../LAVA-M_md5sum.afl_dict <<< "with_dictionary_00 with_dictionary_01 with_dictionary_02 with_dictionary_03 with_dictionary_04"
xargs -n 1 cp -v ../../LAVA-M_md5sum_mutation_seed.txt <<<"with_dictionary_00/afl_in with_dictionary_01/afl_in with_dictionary_02/afl_in with_dictionary_03/afl_in with_dictionary_04/afl_in"
