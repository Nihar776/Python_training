s=[1,2,3,4,5]
# st=map(str,s)
# x=list(st)
# print("This is list of map",x)
# y=tuple(st)
# print("This is tuple of map",y)
# z=set(st)
# print("This is set of map",z)
# print(st)
def multiply(x:int):
    return 2*x
s1=[multiply(x) for x in s]
print("This multiplication is done using loop inside a list: ",s1)

s2=list(map(multiply,s))
print('This is done using Map function: ',s2)

s3 = [(lambda x: x * 2)(x) for x in s]
print("This is done using lambda function: ",s3)

