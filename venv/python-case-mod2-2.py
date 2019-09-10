import sys
import random
b=[]
for x in range(5):
    i = 1
    while not(i%5 == 0 and i%7 == 0) and i not in b:
        i = random.randint(1,1000)
    b.append(i)

print(b)

#a={1,3,6,78,35,55}
# b=[12,24,35,70,88,120,155]
# c=[]
# for x in b:
#     if x%5 == 0 and x%7 == 0:
#         continue
#     else:
#         c.append(x)
# print(c)


# mystr = input('Enter your input: ')
# newd = {}
# if len(mystr)> 0:
#     chrlst = list(mystr)
#     for a in chrlst:
#         i = newd.get(a)
#         if a in newd:
#             newd[a] += 1
#         else:
#             newd[a] = 1
#     for x in newd.keys():
#        print(x,",",newd.get(x))
# else:
#     print('input cant be null')


#print(1/2+2/3+3/4+4/n +n/(n+1))
# liststr = list(mypass)
#newstr='this is forward'
# for x in liststr:
#     if x.isalpha():
#         newstr += x
#


# a=[4,7,3,2,5,9]
# item=0
# for x in a:
#     print("item number %d is %s"%(item,str(x)))
#     item += 1
