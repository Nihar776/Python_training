class Employee:
    def __init__(self,dept:str,role:str,salary:int):
        # self.name=name.capitalize()
        self.role=role.capitalize()
        self.dept=dept.capitalize()
        self.salary=salary

    def showDetails(self)->dict:
        print(f"Department: {self.dept}")
        print(f"Role: {self.role}")
        print(f"Salary : {self.salary}")
        return{'dept':self.dept,'role':self.role,'salary':self.salary}

# askName='Enter Name of the Employee: '
askDept='Enter Department of the Employee: '
askRole='Enter Role of the Employee in that Department : '
askSalary='Enter Salary of the Employee : '

e1=Employee(input(askDept),input(askRole),int(input(askSalary)))
e1.showDetails()