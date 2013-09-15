#!/usr/bin/python

import sys
import re

def filter(line):
    pass

def main(argv):
    line = sys.stdin.readline()
    _line = filter(line)
    pattern = re.compile("[a-zA-Z][a-zA-Z0-9]*")
    try:
        while line:
            for word in  pattern.findall(_line):
                print  word.lower() + "\t" + "1"
            line =  sys.stdin.readline()
    except "end of file":
        return None

if __name__ == "__main__":
    main(sys.argv)
