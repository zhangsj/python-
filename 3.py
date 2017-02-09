#!/usr/bin/env python
#_*_ coding:utf-8 _*_

# Filename : 3.py
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
