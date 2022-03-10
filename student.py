class Person(object):
    def __init__(self,name,aadhar,phone):
        self.name = name
        self.aadhar = aadhar
        self.phone = phone


    def displaydetails(self):
        print(self.name)
        print(self.aadhar)
        print(self.phone)

class Student(Person):
    def __init__(self,name,aadhar,phone,fathername,mothername,hobby):
        self.fathername= fathername
        self.mothername = mothername
        self.hobby = hobby

        Person.__init__(self,name,aadhar,phone)

    def printdetails(self):
        print("Name: ",self.name)
        print("aadhar: ",self.aadhar)
        print("phone: ",self.phone)
        print("fathername: ",self.fathername)
        print("mothername: ",self.mothername)
        print("hobby: ",self.hobby)

x = Student("akash","1234 1234 1234","0987654327","sivamoothy","sumitha","art and dance")
x.printdetails()



