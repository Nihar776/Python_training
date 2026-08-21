from functools import reduce

def add(x,y):
    return x+y

def fact(x,y):
    return x*y

def avg(sum,total_nums):
    return int(sum/total_nums)


lyst=[i for i in range(1,11)]
sumOfLyst=reduce(add,lyst)
print("Sum of number is : ",sumOfLyst)

avg=avg(reduce(add,lyst),len(lyst))
print("Average of number is : ",avg)

fact=reduce(fact,lyst)
print("factorial of 10 is ",fact)