#!/bin/bash

LD_PRELOAD="../libcgc.so ../libtiny-AES128-C.so" ~/fuzzing/AFL/afl-cmin -i mutated_files -o afl_in -- ./$1

#cd mutated_cmin
#for i in mutated_cmin/*; do LD_PRELOAD="../libcgc.so ../libtiny-AES128-C.so" ~/fuzzing/AFL/afl-tmin -i $i -o $i.min \
#-- ../$1;
#done;

#mv *.min ../afl_in
