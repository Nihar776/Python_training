n=int(input("Enter a number to get its Factorial: "))
fact=1
for i in range(2,n+1):
    fact*=i
print(fact,"is the factorial of",n)