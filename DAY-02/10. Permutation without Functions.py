n,r=map(int,(input("Enter n and r for permutation : ").split()))
factn=1
factr=1
i=1
while i<=n:
    factn*=i
    if i<=n-r:
        factr*=i
    i+=1

print(f"{int(factn/factr)} are possible permutation for {n}P{r}")
