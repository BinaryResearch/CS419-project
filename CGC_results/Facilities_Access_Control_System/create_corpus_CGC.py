#!/usr/bin/python3

# use radamsa to mutate /run/utmp

import subprocess
import hashlib
import time
import os
import shutil
import time
import sys
#from tqdm import tqdm  # not installed on server, don't have permisisons


ITERATIONS = 500	  			# number of times radamsa is called to mutate the seed file
MAX_FILE_SIZE = 500				# radamsa-generated files larger than this will be discarded
PATH = "mutated_files"				# directory to write mutated files to
CMIN_PATH = "mutated_cmin"			# subdirectory to write minimized corpus to
TMIN_PATH = "mutated_tmin"			# subdirectory to write minimized files from cmin/ to
FUZZER_DIR_PATH = "/ilab/users/jtd124/fuzzing/AFL/"		# AFL directory
#LD_PRELOAD = 'LD_PRELOAD="../libcgc.so ../libtiny-AES128-C.so" ' # doesn't work with subprocess


# mutate seed file with radamsa
def mutate(seed_file_path):
    output = subprocess.run(["/ilab/users/jtd124/radamsa/bin/radamsa", seed_file_path], stdout = subprocess.PIPE)
    return output.stdout



def minimize_corpus(target_path):
    # Usage: ../../AFL/afl-cmin [ options ] -- /path/to/target_app [ ... ]
    _ = subprocess.run(["./minimize_corpus.sh", target_path])



def main():

    seed_file_path = ""
    target_path = ""
    
    if len(sys.argv) != 3:
        print("usage: ./create_corpus.py [path to input file] [path to target executable]")
        exit(1)
    else:
        for file in [sys.argv[1], sys.argv[2]]:
            if os.path.isfile(file) != True:
                print("file %s not found" % file)

        seed_file_path = sys.argv[1]
        target_path = sys.argv[2]
        

    for dir in [PATH, CMIN_PATH, TMIN_PATH]:
        if not os.path.exists(dir):
            os.makedirs(dir)

    print("[ + ] Generating mutations of %s" % target_path)
    #for i in tqdm(range(1, ITERATIONS)):
    for i in range(1, ITERATIONS):
        if i % 100 == 0:
            print("[ + ] Generating file %d..." % i)
        bytes = mutate(seed_file_path)
        if len(bytes) > MAX_FILE_SIZE:					# smaller files are better
            continue
        filename = hashlib.md5(bytes).hexdigest() + ".txt"	# only unique files will be saved
        with open(PATH + "/" + filename, "wb+") as f:
            f.write(bytes)

    # create corpus from mutated files output by radamsa
    minimize_corpus(target_path)



if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("[ + ] time elapsed: %s" % repr(end - start))
