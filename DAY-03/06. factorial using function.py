def fact(n:int)->int:
    "Return factorial of number"
    factorial=1
    for i in range(1,n+1):
        factorial*=i
    return factorial

num=int(input("Enter a Number to get its factorial: "))
print(fact(num))