def is_even(num:int):
    return num%2==0
def is_negative(num:int):
    return num<0

lyst=[i for i in range(-5,6)]
even= list(filter(is_even,lyst))
print(even)
negative= list(filter(is_negative,lyst))
print(negative)