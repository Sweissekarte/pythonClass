import sys

yournumber = 1

while (yournumber != -1):
    yournumber = int(input('Enter a number between 1 and 10 (enter -1 to exit): '))
    if (yournumber == -1):
        print('goodbye')
        break
    if ((yournumber < 1) | (yournumber > 10)):
        print("you did not follow instructions, try again enter -1 to exit")
        continue
    factor = yournumber
    while (factor > 0 ):
        print (factor*yournumber)
        factor -= 1
    if (yournumber%2) == 0:
        print('your number is evem')
    else:
        print('your number is odd')

