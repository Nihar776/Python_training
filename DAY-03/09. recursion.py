li=[]
def printOnetoN(n:int):

    if n==0:
        return

    li.append(n)
    printOnetoN(n-1)

    print(li[-(n)])

n=int(input("Enter number: "))
printOnetoN(n)