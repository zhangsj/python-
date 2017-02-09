#!/usr/bin/env python
#_*_ coding:utf-8 _*_

#Filename:2.py
# 输入一段语句，统计每个单词出现的次数
txt = raw_input("pls enter some word:")

def coun1(self):
  l = []
  words = self.split()
  for w in words:
    l.append(w)
  for cou in l:
    print cou,"counts:",l.count(cou)
coun1(txt)
