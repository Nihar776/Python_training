class Student:
    def __init__(self,name:str,subjects:list , marks:list):
        self.name=name
        self.marks=marks
        self.subjects=subjects
        # print(f"Student name:{self.name}")

        for i,score in zip(subjects,marks):
            print(i,":",score)
        print(self.calcAverage())

    def calcAverage(self)->float:
        self.avg=sum(self.marks)/len(self.marks)
        print(f"Average score of {self.name} is {(self.avg):.2f}")
        return f"{self.avg:.2f}"

askname="Enter name of the student: "
asksub="Enter names of the subjects in comma separated manner: "
askmarks="Enter marks of 3 subjects in space separated manner: "

student=Student(input(askname),list(input(asksub).split(',')),list(map(float,input(askmarks).split())))