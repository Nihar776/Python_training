class Employee:
    def __init__(self):

        self.dept,self.role,self.salary=(input("Enter Employee details in this format : Department,Role,Salary: ").title()).split(',')
        self.salary=int(self.salary)


    def showDetails(self)->dict:
        print(f"Department: {self.dept}")
        print(f"Role: {self.role}")
        print(f"Salary : {self.salary}")
        return{'dept':self.dept,'role':self.role,'salary':self.salary}


if __name__ == "__main__":
    e1 = Employee()
    e1.showDetails()