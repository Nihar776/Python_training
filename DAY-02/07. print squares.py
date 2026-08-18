n=int(input("Enter a number till you want squares: "))
lyst=[]
for i in range(1,n+1):
    lyst.append(i**2)
print(lyst)
num= int(input("Let's Find a number of your choice : "))
i=-1
while num!=lyst[i]:
    i+=1
    if num==lyst[i]:
        print(f"Found your number: {num} at index: {i}")
        break
    elif i>=len(lyst):
        break
    else: 
        pass