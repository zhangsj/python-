#!/usr/bin/env python
#_*_ coding:utf-8 _*_

#Filename:2.py

txt = raw_input("pls enter some word:")

def coun1(self):
  l = []
  words = self.split()
  for w in words:
    l.append(w)
  for cou in l:
    print cou,"counts:",l.count(cou)
coun1(txt)
