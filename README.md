# CS419-project: AFL

CS419 Computer Security class project. Improve AFL performance with respect to baseline.

Project Description (taken from professor's slides):
 - Improve AFL by any means
   - Seed selection, using metrics other than coverage etc.
 - Test on LAVA-M and Google test suite
 - Compare AFL with your improved version

# Innovation: Corpus Creation via Seed File Mutation

![Corpus generation via mutation](https://github.com/BinaryResearch/CS419-project/blob/master/corpus_generation_pipeline.png)

>Unfortunately, fuzzing is also relatively shallow; blind, random mutations make it very unlikely to reach certain code paths in the tested code, leaving some vulnerabilities firmly outside the reach of this technique.

>There have been numerous attempts to solve this problem. One of the early approaches - pioneered by Tavis Ormandy - is corpus distillation. The method relies on coverage signals to select a subset of interesting seeds from a massive, high-quality corpus of candidate files, and then fuzz them by traditional means. The approach works exceptionally well, but requires such a corpus to be readily available. <sup>1</sup>

Often, no such corpus is available when fuzz testing a binary. Ready-made test cases may also not be available. Using Radamsa (or any other program that can function as a mutation engine), a single well-chosen initial test case can be used to create a corpus tailored specifically to the program to be fuzzed. When combined with other techniques, such as using a custom dictionary, this can result in more unique crashing inputs to be discovered by AFL when fuzzing the target.

# Example Results

![CGC Results](https://github.com/BinaryResearch/CS419-project/blob/master/CGC_results.png)



1. https://github.com/google/AFL/blob/master/README.md
