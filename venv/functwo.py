import os
from funcone import *

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
