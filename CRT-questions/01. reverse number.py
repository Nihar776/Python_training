from math import log10,ceil
def reverseNum(n:int)->int:
    # Edge Case
    if n==0:
        return 0
    
    new_num=0
    no_of_digits=ceil(log10(n))# Get number of digit
    i=1

    while n>0:
        new_num+=(n%10)*(10**(no_of_digits-i))# Append nth last digit to nth place in new number
        n=n//10 # Remove trailing digits that are already appended
        i+=1 # Append to next place
    return new_num


# n=123456
num=int(input("Enter a number to get its palindrome number : "))
print(reverseNum(num))
