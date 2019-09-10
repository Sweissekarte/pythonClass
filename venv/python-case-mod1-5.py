import sys
mynum = int(input('Enter Number to Test:'))

numstring = str(mynum)
liststring = list(numstring)
lenstr = (len(liststring))
Palflag = True
x=1
for i in liststring:
    if i != liststring[lenstr - x]:
        Palflag = False
    x += 1
if Palflag:
    print(liststring, ' is a palindrome')
else:
    print(liststring, ' is not a palindrome')
