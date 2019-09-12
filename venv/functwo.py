import os
from funcone import *
import math

print (addme(5,6,7,8,9,9))
al= myclass()
print(al.pub)
print(al._pro)
print(al._myclass__pri)
print(os.name)
print(os.getcwd())
print(os.path.join('C:\\opt','C:\\users\\marc','C:\\Programs'))
print(os.path)
for i in os.walk(os.getcwd()):
    print(i)
print( dir(math))
a=[100,110,130]
b=[(-1,5)]
print(sum(a))
print(math.atan2(-1,2))