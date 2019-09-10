import sys
mypass = input('Enter password to verify: ')
lowerletter,upperletter, digit,specialchar,special = False, False,False,False,{'$','#','@'}

validation={'maxlength':'too long must be less than 12 char','minlength':'not long enough must be > 6 char',
            'special':'must contain a special char ($#@)','upper':'must contain a capital letter',
            'number':'must contain a number','lower':'must contain lower case letter'}
liststr = list(mypass)
for x in liststr:
    if x.isdigit():
        digit=True
    if x.isalpha():
        print (lowerletter or x.islower())
        lowerletter = lowerletter or x.islower()
        upperletter = upperletter or not x.islower()
    if x in special:
        specialchar = True

reason = validation['minlength'] if 6>len(mypass) else validation['maxlength'] if 12<len(mypass) else validation['lower'] \
    if not lowerletter else validation['upper'] if not upperletter else validation['number'] if not digit else validation['special'] \
    if not specialchar else'success'

print(reason)