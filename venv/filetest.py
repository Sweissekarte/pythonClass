import os

class client_p:
    minage=0
    maxage=0
    profession=""
    def __init__(self,age,profession):
        self.profession = profession
        self.minage = age
        self.maxage = age
    def __str__(self):
        return "Role: " + self.profession + "  Min Age: " + str(self.minage) + "  Max Age: " + str(self.maxage)
    def setAge(self,age):
        self.minage = age if age < self.minage else self.minage
        self.maxage = age if age > self.maxage else self.maxage
    def setMinage(self,age):
        self.minage = age
    def getMinage(self):
        return(self.minage)
    def setMaxAge(self,age):
        self.maxage = age
    def getMaxAge(self,age):
        retunr(self.maxage)

newfile = open('bank-data.csv',"r")
mylist = []
professions = {}
#newfile.write("Hi My name is harold")
f1 = newfile.readlines()
firstline = True
for x in f1:
    if firstline:
        firstline = False
        continue
    datarow = x.split(",")
    role, age = datarow[1], int(datarow[0])
#    print(datarow[0],datarow[1])
    if len(mylist) == 0:
        mylist.append(client_p(age, role))
    addme=True
    for row in mylist:
        if role in row.profession:
            row.setAge(age)
            addme = False
            break
    if addme:
         mylist.append(client_p(age,role))
 #           print("add row")

    if datarow[1] in professions.keys():
        ages = professions.get(datarow[1]).split(",")
        ages[0] = str(age) if age < int(ages[0]) else ages[0]
        ages[1] = str(age) if age > int(ages[1]) else ages[1]
        professions[role] = str(ages[0] + "," + ages[1])
    else:
        professions[role] = str(age) + "," + str(age)

newfile.close()

successmsg = ""
while role != "END":
    clientstr = input("Enter your profession, age (Enter END to exit) to check eligibility: ")
    clientdata = clientstr.split(",") if "," in clientstr else [clientstr,0]
    role, age = clientdata[0],int(clientdata[1])
    Eligible = False
    for row in mylist:
        if role.lower() in row.profession.lower():
            if row.minage <= age <= row.maxage:
                Eligible = True
            break
    successmsg = "Have a nice day - exiting" if role =="END" else "You are Eligible !!" if Eligible else "You are not Eligible."
    print(successmsg)
#mylist.append(client_p(int(datarow[0]),datarow[1]))

# nums= set([11,2,3,3,3,4,4])
# print(len(nums))
#
# d={'john':40,'peter':45}
# print(list(d.keys()))