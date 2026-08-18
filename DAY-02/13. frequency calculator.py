arr= list(map(int,input("Enter space separed numbers: ").split()))
dic={}
unique_char= list(set(arr))
for i in unique_char:
    dic[i]=arr.count(i)

print(dic)