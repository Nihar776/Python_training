n=int(input("Enter a number : "))
print(f"{int(n*(n+1)/2)} is the sum of {n} natural number Using formula")
sum=0
i=1
while i<=n:
    sum+=i
    i+=1
print(f"{sum} is the sum of {n} natural number Using While loop")
