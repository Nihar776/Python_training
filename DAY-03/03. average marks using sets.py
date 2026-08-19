n=int(input("Enter number of marks you want to enter: "))
marks=[]
for i in range(n):
    name,mark = input("Enter Name and marks serated by comma (eg: Nihar,95): ").split(',')
    marks.append((name,int(mark)))
    
# marks=[('Alice',85),('Bob',90),('Alice',83)]

total_marks={}

for student in marks:
    if total_marks.get(student[0])==None:
        total_marks[student[0]]=[student[1]]

    else:
        total_marks[student[0]].append(student[1])
        # total_marks[student[0]][1]+=1

# print(total_marks)
names=set(marks[i][0] for i in range(n))

for student,name in zip(total_marks,names): 
    avg_marks=sum(total_marks[student])/len(total_marks[student])
    print(f"{name} has average marks of {avg_marks}")