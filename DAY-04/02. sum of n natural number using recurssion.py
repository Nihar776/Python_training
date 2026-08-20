def sumOfN(n:int)->int:
    if n==1:
        return 1
    return n+sumOfN(n-1)
n=int(input("Enter a number N to get sum of N Natural numbers: "))
print(f"Sum of {n} Natural number is {sumOfN(n)}")