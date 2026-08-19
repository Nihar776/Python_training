def fact(n:int)->int:
    "Return factorial of number"
    factorial=1
    for i in range(1,n+1):
        factorial*=i
    return factorial

def PnC(choice:int,n:int,r:int)->int:
    P=int(fact(n)/fact(n-r))
    if choice==1:
        print(f"There are {P} possible Permutations of arranging {r} objects in {n} ways.")
        return P
    elif choice==2:
        C=int(P/fact(r))
        print(f"There are {C} possible Combination of choosing {r} objects from {n} objects.")
        return C
    else:
        print("Invalid input.")


choice=int(input("Enter '1' for calculating Permutations\nEnter '2' for calculating Combinations\n"))
n,r = map(int,input("Enter values of n and r respectively in comma separed manner(eg:5,4): ").split(','))
PnC(choice,n,r)
