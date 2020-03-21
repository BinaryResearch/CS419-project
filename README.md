# CS419-project
CS419 Computer Security class project. Improve AFL performance with respect to baseline.

We could choose 1 project from among 4 topics:
 1) Creating a cryptography platform that allow users/attackers to encrypt and decrypt messages, supports multiple modes, etc.
 2) Improving AFL performance in some way
 3) Creating a protected file system with granular per-user permissions/access control
 4) Adversarial machine learning - creating a platform for attack and defense

# AFL

Project Description (taken from professor's slides):
 - Improve AFL by any means
   - Seed selection, using metrics other than coverage etc.
 - Test on LAVA-M and Google test suite
 - Compare AFL with your improved version
 
At minimum:
 - Implementing at least one improvement
 - Tests on LAVA-M and Google Test Suite (AFL and improved version)
 
Requirements:
 - You can re-use tools like KLEE (for symbolic execution) etc
 - You cannot re-use existing fuzzerslike Driller
 - How to evaluate fuzz testing?
   - https://www.cs.umd.edu/~mwh/papers/fuzzeval.pdf
 
