#!/usr/bin/python3

# use radamsa to mutate /run/utmp

import subprocess
import hashlib
import time
import os
import shutil
import time
#from tqdm import tqdm  # not installed on server, don't have permisisons


ITERATIONS = 100				# number of times radamsa is called to mutate the seed file
MAX_FILE_SIZE = 2000				# radamsa-generated files larger than this will be discarded
PATH = "mutated_files"				# directory to write mutated files to
CMIN_PATH = "mutated_cmin"			# subdirectory to write minimized corpus to
TMIN_PATH = "mutated_tmin"			# subdirectory to write minimized files from cmin/ to
SEED_FILE_PATH = "./LAVA-M_uniq_mutation_seed.txt"	# path to seed file
FUZZER_DIR_PATH = "/ilab/users/jtd124/fuzzing/AFL/"		# AFL directory
TARGET_PATH = "./LAVA-M_uniq"


# mutate seed file with radamsa
def mutate():
    output = subprocess.run(["/ilab/users/jtd124/radamsa/bin/radamsa", SEED_FILE_PATH], stdout = subprocess.PIPE)
    return output.stdout



# THE '@@' AT THE END IS ABSOLUTELY VITAL - THIS METHOD FAILS WITHOUT IT
def minimize_corpus():
    # Usage: ../../AFL/afl-cmin [ options ] -- /path/to/target_app [ ... ] @@

    files = os.listdir(CMIN_PATH)
    if len(files) != 0:
        print("%s not empty, recreating directory..." % CMIN_PATH)
        shutil.rmtree(CMIN_PATH)
        os.makedirs(CMIN_PATH)

    print("[ + ] Minimizing corpus")
    afl_cmin = FUZZER_DIR_PATH + "/afl-cmin"
    output = subprocess.run([afl_cmin, "-i", PATH, "-o", CMIN_PATH, "--", TARGET_PATH, '@@'])
    #out = output.stdout.decode("ASCII").split("\r")

    # minimize files
    minimize_corpus_files()



def minimize_corpus_files():
    print("[ + ] Minimizing files. Press CTRL-C now to abort.")
    time.sleep(5)
    print("[ + ] Proceeding...")
    afl_tmin = FUZZER_DIR_PATH + "/afl-tmin"
    files = os.listdir(CMIN_PATH)
    num_files = len(files)
    i = 1
    #for file in tqdm(files):
    for file in files:
        print("\n[ + ] Minimizing file %d / %d" % (i, num_files))
        file_path = CMIN_PATH + "/" + file
        output = subprocess.run([afl_tmin, "-i", file_path, "-o", file + ".min", "--", TARGET_PATH, "@@" ],
                                stdout = subprocess.PIPE)
        shutil.move(file + ".min", TMIN_PATH)
        i += 1


def main():

    for dir in [PATH, CMIN_PATH, TMIN_PATH]:
        if not os.path.exists(dir):
            os.makedirs(dir)

    print("[ + ] Generating mutations of %s" % TARGET_PATH)
    #for i in tqdm(range(1, ITERATIONS)):
    for i in range(1, ITERATIONS):
        if i % 10 == 0:
            print("[ + ] Generating file %d..." % i)
        bytes = mutate()
        if len(bytes) > MAX_FILE_SIZE:					# smaller files are better
            continue
        filename = hashlib.md5(bytes).hexdigest() + ".txt"	# only unique files will be saved
        with open(PATH + "/" + filename, "wb+") as f:
            f.write(bytes)

    # create corpus from mutated files output by radamsa
    minimize_corpus()



if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("[ + ] time elapsed: %s" % repr(end - start))
