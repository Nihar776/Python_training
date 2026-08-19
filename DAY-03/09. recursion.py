def printOnetoN(n:int,i:int):
    if n ==i-1:
        return

    print(i)

    printOnetoN(n,i+1)
n=int(input("Enter number: "))
printOnetoN(n,1)