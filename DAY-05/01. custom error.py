class NegativeNumberError(Exception):

    pass
try: 
    n=int(input("Enter your Age: "))
    if n<0: 
        raise NegativeNumberError()
        

except :
    print("Age cannot be negative. ")
    
