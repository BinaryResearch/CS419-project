#!/usr/bin/python3

import sys
import subprocess
from pathlib import Path


# this program extracts and createsa dictionary all of byte constants used in comparisons in the object
# code of the target program. The output of objdump is parsed such that values used with the 'cmp' instruction
# are converted into the format AFL expects in a dictionary.
#
# this approach is especially effective when fuzzing the LAVA-M binaries, since many of the bugs are
# follow such comparisons.
#
# idea from http://moyix.blogspot.com/2016/07/fuzzing-with-afl-is-an-art.html

def main():
    if len(sys.argv) != 2:
        print("usage: ./create_AFL_dict.py <full path of target binary>")
        exit(1)
    else:
        file = Path(sys.argv[1])
        if file.is_file() != True:
            print("file %s not found, exiting." % sys.argv[1])

    output = subprocess.run(["objdump", "-dj", ".text", file], stdout = subprocess.PIPE)
    lines = output.stdout.split(b'\n')

    strings = []
    for line in lines:
        if b'cmp' in line:
            split_1 = line.split(b'$')
            if len(split_1) > 1:
                string_literal = split_1[1].split(b',')[0].decode('ascii').split('x')[1]
                string_literal_bytes = [string_literal[i:i+2] for i in range(0, len(string_literal), 2)]
                byte_string = ''
                for byte in string_literal_bytes:
                    if len(byte) == 1:
                        byte = '0' + byte
                    byte_string += ('\\x' + byte)
                strings.append('"' + byte_string + '"' + '\n')

    print(sys.argv[1].split("/")[-1:][0])
    outfile = sys.argv[1].split("/")[-1:][0] + ".afl_dict"
    with open(outfile, "w") as f:
        for string in set(strings):
            f.write(string)


if __name__ == "__main__":
    main()
