s=[1,2,3,4,5]
st=map(str,s)
x=list(st)
print("This is list of map",x)
y=tuple(st)
print("This is tuple of map",y)
z=set(st)
print("This is set of map",z)
print(st)
def multiply(x:int):
    return 2*x

s2=list(map(multiply,s))
print(s2)