#!/usr/bin/python
# this is the mapper in map-reduce job 
# main function in this mapper:
# 1. get the date info from the file name
# 2. aggreate the hr PV to day PV
# 3. send key value pair to the map-reduce egine

import re
import operator

# filter logic
# 1. only keep "en" project
# 2. excluede Special Pages
# 3. filter out lowerEnglish begining, retain non-english titles
# 4. filter out image
# 5. filter out auto-gen page, like 4040_error

#using regular expression, give four group of re pattern.
pattern_project_name =  re.compile(r"^en\Z")
pattern_special_page = re.compile(r"^([a-z]+|Media|Special|Talk|User|User_talk|Project|Project_talk|File|File_talk|MediaWiki|MediaWiki_talk|Template|Template_talk|Help|Help_talk|Category|Category_talk|Portal|Wikipedia|Wikipedia_talk).*")
pattern_img_type = re.compile(r".*\.(jpg|gif|png|JPG|GIF|PNG|txt|ico)\Z")
pattern_boilerplate = re.compile(r"^(404_error/|Main_Page|Hypertext_Transfer_Protocol|Favicon\.ico|Search)\Z")

fileinput = open ('pagecounts-20130601-000000')
fileHandle = open ('test.txt','w')
writebuffer = []
for line in fileinput:
    array = line.split()
    if pattern_title.match(array[0]) and not pattern_fileType.match(array[1]) and not pattern_specialPage.match(array[1]) and not pattern_boilerplate.match(array[1]):
        fileHandle.write(array[1]+'\t'+array[2]+'\n')
fileinput.close()
fileHandle.close()

