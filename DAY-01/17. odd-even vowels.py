def totalVowel(a:str)-> int:
    sum=a.count("a") + a.count("i")+ a.count("o")+ a.count("u")+ a.count("e")
    return sum
    
s1,s2=input("Enter a string : ").lower().split()
sum=totalVowel(s1)+totalVowel(s2)
if sum%2==0:
    print("Perfect Match")
else:
    print("Average Match")