import sys

instring = input('Enter words separated by comma: ')
direct = input('Enter direction of sort (a)A-Z (d)Z-A (default is a): ')
if direct != 'd':
    direct = 'a'
wordlist = instring.split(",")
if direct == 'd':
    wordlist.sort(reverse=True)
else:
    worlist.sort
#for word in newwordlist
print(wordlist)

