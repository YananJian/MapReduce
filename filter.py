import re
import operator
pattern_title =  re.compile(r"^en\Z")
#pattern_num = re.compile(r".*\t(\d+)\n")
pattern_specialPage = re.compile(r"^([a-z]+|Media|Special|Talk|User|User_talk|Project|Project_talk|File|File_talk|MediaWiki|MediaWiki_talk|Template|Template_talk|Help|Help_talk|Category|Category_talk|Portal|Wikipedia|Wikipedia_talk).*")
pattern_fileType = re.compile(r".*\.(jpg|gif|png|JPG|GIF|PNG|txt|ico)\Z")
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

