import os

class Error(Exception):
    pass

class CustomerNotAllowed(Error):
    pass

class Customer:
    title = ""
    fname = ""
    lname = ""
    isblacklisted = False;

    def __init__(self,last,first,bl):
        self.lname = last.strip()
        str = first.index(".") + 1
        self.title = first[0:str]
        self.isblacklisted = True if int(bl) == 1 else False
        self.fname = first[len(self.title) + 1:len(first) - 1]
  #      print(self)

    def __str__(self):
        return "Title:" + self.title + " First Name:" + self.fname + " Last Name:" + self.lname + " Blacklisted:" + str(self.isblacklisted)

class Order(Customer):
    product_name = ""
    product_code = ""

    def __init__(self, Customer,product,code):
        self.title = Customer.title
        self.fname = Customer.fname
        self.lname = Customer.lname
        self.product_code = product
        self.product_name = code

    def setProductName(self,product):
        self.product_name = product

    def setProductCode(self,code):
        self.product_code = code


    def __str__(self):
        return "Title:" + self.title + " First Name:" + self.fname + " Last Name:" + self.lname + \
               " Product ordered: " + self.product_name + " Product Code: " + self.product_code
    #   self.product_name = product
     #   self.product_code = code

def createOrder(Customer):
    try:
        if Customer.isblacklisted:
 #           print ("%s %s %s is Blacklisted." %(Customer.title,Customer.fname,Customer.lname))
            raise CustomerNotAllowed
        else:
            custorder = createOrder2(Customer,"new car","A1B2")
            return custorder
    except CustomerNotAllowed:
        return "Customer Not allowed"

def createOrder2(Customer,product,code):
    neworder = Order(Customer,product,code)
    return neworder
 #   else:
 #       print ("%s %s %s can order." %(Customer.title,Customer.fname,Customer.lname), Customer.isblacklisted)


newfile = open('FairDealCustomerData.csv',"r")
mylist = []

blacklist = 0
f1 = newfile.readlines()
for x in f1:
    data = x.split(",")
    if len(mylist) == 0:
        mylist.append(Customer(data[0],data[1],data[2]))
    addme=True
    for row in mylist:
        if data[0] in row.lname:
            addme = False
            break
    if addme:
         mylist.append(Customer(data[0],data[1],data[2]))
         if int(data[2]) == 1:
             blacklist += 1

newfile.close()

for row in mylist:
   message = createOrder(row)
   if row.isblacklisted == False:
       print(message)
 #   blacklist += 1 if row.isblacklisted == True else blacklist
print("There are %d Customers and %d blacklisted customers" %(len(mylist),blacklist))
