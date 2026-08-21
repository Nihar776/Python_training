from math import log10,ceil
def is_palindrome(num:int):
    length=ceil(log10(num))
    reverse=0
    original=num
    while original>0:
        reverse+=(original%10)*10**(length-1)
        original=original//10
        length-=1
    return num==reverse

# n=12344321
n=int(input("Enter a number to check if its palindrome: "))
print(is_palindrome(n))