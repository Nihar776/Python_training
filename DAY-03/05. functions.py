def length(l:list)->int:
    "Return number of element in the list"
    return len(l)
def printList(l:list)->None:
    "Prints every element in the list in single line"
    for i in l:
        print(i ,end=" ")

lyst=[False,True,2,3,'Four','Five','Six',7.0,8.0,9.0]
print(length(lyst))
printList(lyst)