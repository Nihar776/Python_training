a,b,c= map(int,(input("Enter 3 numbers: ").split()))

if a==b==c: 
    print("All numbers are equal")
elif a>b and a>c:
    print(a, "is the Largest Number out of ",a,b,c)
elif b>a and b>c:
    print(b, "is the Largest Number out of ",a,b,c)
else: 
    print(c, "is the Largest Number out of ",a,b,c)

