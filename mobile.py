class Mobile:
    def __init__(self,mobilename,mobilebrand,mobileprice,lanchyear):
        self.mobilename = mobilename
        self.mobilebrand = mobilebrand
        self.mobileprice = mobileprice
        self.lanchyear = lanchyear

    def printdata(self):
        print(self.mobilename)
        print(self.mobilebrand)
        print(self.mobileprice)
        print(self.lanchyear)

Data = Mobile(input("enter the mobile name:"),input("enter the mobile brand:"),input("enter the mobile price:"),input("enter the lanch year:"))


Data.printdata()