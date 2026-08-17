s=input("Enter a string : ").lower()
sum=s.count("a") + s.count("i")+ s.count("o")+ s.count("u")+ s.count("e")
if sum%2==0:
    print("Perfect Match")
else:
    print("Average Match")