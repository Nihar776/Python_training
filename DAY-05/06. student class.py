class Student:
    def __init__(self,name:str,marks:list):
        self.name=name
        self.marks=marks
        # print(f"Student name:{self.name}")

        for i,score in enumerate(marks):
            print(f"Subject-0{i+1}:",score)
        print(self.calcAverage())

    def calcAverage(self)->float:
        self.avg=sum(self.marks)/len(self.marks)
        print(f"Average score of {self.name} is {(self.avg):.2f}")
        return f"{self.avg:.2f}"



student=Student(input("Enter name of the student: "),list(map(float,input("Enter marks of 3 subjects in space separated manner: ").split())))