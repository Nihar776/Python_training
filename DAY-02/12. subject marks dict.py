di={}
n=int(input("How many subjects you have: "))
for i in range(n):
    name=input("Name of subject: ")
    di[name]=int(input(f"Enter marks of {name}: "))
for sub , marks in zip(di.keys(),di.values()):
    print(f"You scored {marks} in {sub}")