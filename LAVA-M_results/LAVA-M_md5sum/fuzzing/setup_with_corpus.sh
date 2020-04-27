#!/bin/bash

cd with_corpus
mkdir with_corpus_0{0..4}
mkdir with_corpus_0{0..4}/afl_in
mkdir with_corpus_0{0..4}/afl_out

xargs -n 1 cp -v ../../LAVA-M_md5sum <<< "with_corpus_00 with_corpus_01 with_corpus_02 with_corpus_03 with_corpus_04"
xargs -n 1 cp -v ../../mutated_tmin/* <<< "with_corpus_00/afl_in with_corpus_01/afl_in with_corpus_02/afl_in with_corpus_03/afl_in with_corpus_04/afl_in"
