#!/usr/bin/env python
#_*_ coding:utf-8 _*_

# Filename : 3.py
# 输入一段去重，并保存到文件。存在问题 保存的为乱码
import pickle
txt = raw_input("pls enter somethting:")

def savef(self,filename):
  f = open(filename,"w")
  words = set(self.split())
  out = [i for i in words]
  pickle.dump(out,f)
  f.close()
  f = open(filename,"r")
  w = pickle.load(f)
  print  w
  f.close()
savef(txt,"1")
