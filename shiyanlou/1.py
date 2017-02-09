#!/usr/bin/env python
#_*_ coding:utf-8 _*_

# Filename : 1.py
# 输入一个数字，打印出0到这个数之间的素数
m = int(raw_input("pls enter a num: "))

def s(n):
  for i in range(2,n):
    if n % i == 0:
      return False
  return True
for m in range(2,m+1):
  if s(m):
    print m
