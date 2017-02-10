#!/usr/bin/env python
#_*_ coding:utf-8 _*_

#Filename: 4.py
# 请定义一个动物类里面有一个吠叫的方法，然后再定义一个猫的类和狗的类都继承动物类，并重写吠叫的方法，猫输出miaomiao，狗输出wangwang，最后生成它们的实例，调用一下方法。
class animals:
  def speak(self):
    print ("the different speak")
class dog(animals):
  def speak(self):
    print ("dog is speak wangwang!")
class cat(animals):
  def speak(self):
    print ("cat is speak miaomiao!")
if __name__ == "__main__":
  c=cat()
  c.speak()
  d=dog()
  d.speak()

