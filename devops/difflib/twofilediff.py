#!/usr/bin/env python
#coding:utf-8
# run as: python towfilediff.py file1 file2 > diff.html
import difflib
import sys

try:
    textfile1=sys.argv[1]
    textfile2=sys.argv[2]
except Exception,e:
    print "Error:"+str(e)
    print "Usage: 3.py filename1 filename2"
    sys.exit()

def readlie(filename):
    try:
        fileHandle = open (filename,'rb')
        text=fileHandle.read().splitlinex()
        fileHandle.close()
        return text
    except IOError as error:
        print ('Read file Error:'+str(error))
        sys.exit()

if textfile1 == "" or textfile2=="":
    print "Usage:3.py filename1 filename2"
    sys.exit()

text1_lines = readfile(textfile1)
text2_lines = readfile(textfile2)

d = difflib.HtmlDiff()
print d.make_file(text_lines,text2_lines)
