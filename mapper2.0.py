#!/usr/bin/python
from __future__ import print_function
import sys
import re
import os

#using the patterns in filter

def main(argv):
    pattern1 = re.compile(r"^en\Z")
    pattern2 = re.compile(r"^([a-z]+|Media|Special|Talk|User|User_talk|Project|Project_talk|File|File_talk|MediaWiki|MediaWiki_talk|Template|Template_talk|Help|Help_talk|Category|Category_talk|Portal|Wikipedia|Wikipedia_talk).*")
    pattern3 = re.compile(r".*\.(jpg|gif|png|JPG|GIF|PNG|txt|ico)\Z")
    pattern4 = re.compile(r"^(404_error/|Main_Page|Hypertext_Transfer_Protocol|Favicon\.ico|Search)\Z")
    for line in sys.stdin:
        
        if  not pattern1.search(line):
            continue
        if pattern2.search(line):
            continue
        if pattern3.search(line):
            continue
        if pattern4.search(line):
            continue
    
        tmp = line.split(' ')
        date = os.environ["map_input_file"].split('-')[1]
        if len(tmp) > 2:
            print (tmp[1] +'\t'+date+'\t'+ tmp[2])

if __name__ == '__main__':
    main(sys.argv)
