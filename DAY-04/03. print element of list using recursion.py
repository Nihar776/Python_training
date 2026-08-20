def printlist(li:list,i=0)->None:
    if i==len(li):
        return
    print(li[i])
    printlist(li,i+1)

lyst=input("Enter a list in space separated manner: ").split()

printlist(lyst)