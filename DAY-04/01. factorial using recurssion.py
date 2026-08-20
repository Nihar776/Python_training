def fact(n:int)->int:
    if n==0 or n==1:
        return 1
    return n*fact(n-1)

n=int(input("Enter a number to get its factorial: "))
print(f"{n}!={fact(n)}")