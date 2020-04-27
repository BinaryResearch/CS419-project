#!/bin/bash

cd baseline/
~/fuzzing/AFL/afl-plot baseline_00/afl_out/ baseline_00/baseline_00_plot
~/fuzzing/AFL/afl-plot baseline_01/afl_out/ baseline_01/baseline_01_plot
~/fuzzing/AFL/afl-plot baseline_02/afl_out/ baseline_02/baseline_02_plot
~/fuzzing/AFL/afl-plot baseline_03/afl_out/ baseline_03/baseline_03_plot
~/fuzzing/AFL/afl-plot baseline_04/afl_out/ baseline_04/baseline_04_plot

cp -v -r baseline_00/baseline_00_plot/ baseline_plots/
cp -v -r baseline_01/baseline_01_plot/ baseline_plots/
cp -v -r baseline_02/baseline_02_plot/ baseline_plots/
cp -v -r baseline_03/baseline_03_plot/ baseline_plots/
cp -v -r baseline_04/baseline_04_plot/ baseline_plots/

cd ../with_corpus/
~/fuzzing/AFL/afl-plot with_corpus_00/afl_out/ with_corpus_00/with_corpus_00_plot
~/fuzzing/AFL/afl-plot with_corpus_01/afl_out/ with_corpus_01/with_corpus_01_plot
~/fuzzing/AFL/afl-plot with_corpus_02/afl_out/ with_corpus_02/with_corpus_02_plot
~/fuzzing/AFL/afl-plot with_corpus_03/afl_out/ with_corpus_03/with_corpus_03_plot
~/fuzzing/AFL/afl-plot with_corpus_04/afl_out/ with_corpus_04/with_corpus_04_plot

cp -v -r with_corpus_00/with_corpus_00_plot/ with_corpus_plots/
cp -v -r with_corpus_01/with_corpus_01_plot/ with_corpus_plots/
cp -v -r with_corpus_02/with_corpus_02_plot/ with_corpus_plots/
cp -v -r with_corpus_03/with_corpus_03_plot/ with_corpus_plots/
cp -v -r with_corpus_04/with_corpus_04_plot/ with_corpus_plots/

cd ../with_dictionary/
~/fuzzing/AFL/afl-plot with_dictionary_00/afl_out/ with_dictionary_00/with_dictionary_00_plot
~/fuzzing/AFL/afl-plot with_dictionary_01/afl_out/ with_dictionary_01/with_dictionary_01_plot
~/fuzzing/AFL/afl-plot with_dictionary_02/afl_out/ with_dictionary_02/with_dictionary_02_plot
~/fuzzing/AFL/afl-plot with_dictionary_03/afl_out/ with_dictionary_03/with_dictionary_03_plot
~/fuzzing/AFL/afl-plot with_dictionary_04/afl_out/ with_dictionary_04/with_dictionary_04_plot

cp -v -r with_dictionary_00/with_dictionary_00_plot/ with_dictionary_plots/
cp -v -r with_dictionary_01/with_dictionary_01_plot/ with_dictionary_plots/
cp -v -r with_dictionary_02/with_dictionary_02_plot/ with_dictionary_plots/
cp -v -r with_dictionary_03/with_dictionary_03_plot/ with_dictionary_plots/
cp -v -r with_dictionary_04/with_dictionary_04_plot/ with_dictionary_plots/

cd ../with_all/
~/fuzzing/AFL/afl-plot with_all_00/afl_out/ with_all_00/with_all_00_plot
~/fuzzing/AFL/afl-plot with_all_01/afl_out/ with_all_01/with_all_01_plot
~/fuzzing/AFL/afl-plot with_all_02/afl_out/ with_all_02/with_all_02_plot
~/fuzzing/AFL/afl-plot with_all_03/afl_out/ with_all_03/with_all_03_plot
~/fuzzing/AFL/afl-plot with_all_04/afl_out/ with_all_04/with_all_04_plot

cp -v -r with_all_00/with_all_00_plot/ with_all_plots/
cp -v -r with_all_01/with_all_01_plot/ with_all_plots/
cp -v -r with_all_02/with_all_02_plot/ with_all_plots/
cp -v -r with_all_03/with_all_03_plot/ with_all_plots/
cp -v -r with_all_04/with_all_04_plot/ with_all_plots/
