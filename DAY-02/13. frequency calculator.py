arr= list(map(int,input("Enter space separed numbers: ").split()))
dic={}
for i in arr: 
    if dic.get(i)==None:
        dic[i]=1
    else:
        dic[i]+=1

print(dic)