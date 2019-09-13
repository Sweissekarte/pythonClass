class Customer:
    title = ""
    fname = ""
    lname = ""
    isblacklisted = 0;

    def __init__(self,last,first,bl):
        self.lname = last
        str = first.index(".") + 1
        self.title = first[0:str]
        self.isblacklisted = bl
        self.fname = first[len(self.title):len(first) - 1]

    def __str__(self):
        return "Title:" + self.title + " First Name:" + self.fname + " Last Name:" + self.lname + " Blacklisted:" + self.isblacklisted

    def setIsblacklisted(self,isblacklisted):
        self.isblacklisted = isblacklisted

    def isblacklisted(self):
        return self.isblacklisted

    def setTitle(self,title):
        self.title = title

    def getTitle(self):
        return self.title

    def setFname(self,fname):
        self.fname = fname

    def getFname(self):
        return self.fname

    def setLname(self,lname):
        self.lname = lname

    def getLname(self):
        return self.lname

class Order:
    productname=""
    productcode=0
    def __init__(self,product, code):
        self.productcode = code
        self.productname = product
    def __str__(self):
        return self.productname + ", " + str(self.productcode)

# customer1 = Customer()
# customer1.setTitle("Mr.")
# customer1.setFname("Barack")
# customer1.setLname("Obama")
#
# customer2 = Customer()
# customer2.setTitle("Mrs.")
# customer2.setFname("George")
# customer2.setLname("Bush")
#
# print("First Customer Title %s" , customer1.getTitle())
# print("Second Customer Title %s" , customer2.getTitle())
# print("First Customer Title %s" , customer1.getTitle())

