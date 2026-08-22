from method_in_class import Employee

class Engineer(Employee):
    def __init__(self):
        self.name,self.age=input("Enter Name and Age in comma separated way (Name,Age): ").split(',')
        self.age=int(self.age)
        super().__init__()

    def showDetails(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        details=super().showDetails()
        details['name']=self.name
        details['age']=self.age
        return details
    


e1=Engineer()
details=e1.showDetails()
print(details)
