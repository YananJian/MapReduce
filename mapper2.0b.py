#!/usr/bin/python
from __future__ import print_function
import sys
import re
import os

def main(argv):
    pattern1 = re.compile(r'^en ')
    pattern2 = re.compile(r'^en [a-z]')
    pattern3 = re.compile(r'^en (Media|Special|Talk|User|User_talk|Project|Project_talk|File|File_talk|MediaWiki|MediaWiki_talk|Template|Template_talk|Help|Help_talk|Category|Category_talk|Portal|Wikipedia|Wikipedia_talk)')
    pattern4 = re.compile(r'\.(ico|jpg|gif|png|JPG|PNG|txt) [0-9]')
    pattern5 = re.compile(r'en (Main_Page|Hypertext_Transfer_Protocol|404_error/|Favicon.ico Search) [0-9]')
    for line in sys.stdin:
        
        if  not pattern1.search(line):
            continue
        if pattern2.search(line):
            continue
        if pattern3.search(line):
            continue
        if pattern4.search(line):
            continue
        if pattern5.search(line):
            continue
         
        tmp = line.split(' ')
        date = os.environ["map_input_file"].split('-')[1]
        if len(tmp) > 2:
            print (tmp[1] +'\t'+date+'\t'+ tmp[2])

if __name__ == '__main__':
    main(sys.argv)
