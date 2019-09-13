import math
#
# coords = input("enter moves comma list UP,DOWN,LEFT,RIGHT: ")
#
# coord_list = coords.split(",")
# Y = int(coord_list[0]) - int(coord_list[1])
# X = int(coord_list[2]) - int(coord_list[3])
#
# print("Distance relative to 0,0 is: %f" % (math.atan2(X,Y)))


# import time
#
# now = time.localtime()
#
# print("Day time!") if  6<= now.tm_hour <= 19 else Print("Night Time")

# def getsqrt(in_side):
#     C=50
#     H=30
#     Q= math.sqrt((2*C*in_side)/H)
#     return int(Q)
#
# D_list = input("Enter comma separated list of numbers to compute: ")
#
# D = D_list.split(",")
#
# for i in D:
#     print("Compute value of %d is %d" %(int(i),getsqrt(int(i))))

# def factor(myint):
#     if myint > 1:
#         myint *= factor(myint - 1)
#         return myint
#     else:
#         return 1
#
# mynum = int(input("Enter number for Factorial: "))
# rfactor = mynum
# factorial = 0
# if mynum > 0:
#     factorial = mynum
#     while mynum > 1:
#         mynum -= 1
#         factorial *= mynum
# else:
#     print("number must be greater than 0")
#
# print("Factorial is: ", factorial)
# print ("Factorial is:", factor(rfactor))

#
# b=[]
# for i in range(2000, 3200):
#     if (i%5 > 0 and i%7 == 0):
#         b.append(i)
#
# print(b)
# print(dir(math))
# a = [5,6,3,8]
# print(sum(a))

# import sys
#
# instring = input('Enter Sentence: ')
# numitems = len(instring)
# i=0
# lower,upper = 0,0
# while i < numitems:
#     if instring[i].isupper():
#         upper += 1
#     elif instring[i].islower():
#         lower += 1
#     i += 1
#
# print('Lower: ',lower,'\nUpper: ',upper)

x= input("Enter binary number list: ")
c = x.split(",")
b=[]
for i in c:
    if (int(i)%5 == 0):
        b.append(i)

print(b)