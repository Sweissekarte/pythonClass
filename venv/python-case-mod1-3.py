import sys
First_num = 1000
Last_num = 3000

while First_num < Last_num:
    numstring = str(First_num)
    liststring = list(numstring)
    evenflag = True
    for i in liststring:
        if int(i)%2 != 0:
            evenflag = False
    if evenflag:
        print(liststring)
    First_num += 1