import sys

instring = input('Enter Sentence: ')
numitems = len(instring)
i=0
Letters,digits = 0,0
while i < numitems:
    if instring[i].isdigit():
        digits += 1
    else:
        Letters += 1
    i += 1

print('Letters: ',Letters,'\nDigits: ',digits)

