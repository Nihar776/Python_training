a=0
while(a<3):
    if(a<1):
        name=input("Enter your full name: ").strip()
        if name.count(" ")==0:
            print("Name must contain first name and last name!")
            name=input("Enter Full name : ")
        else:
            a=1
    if(a<2 and a==1):
        email=input("Enter an Email id: ")
        if (email.endswith(".com") or email.endswith(".org")) and email.find("@")!=-1 :
            print("Valid Email Id")
            a+=1
        else:
            print("Inalid Email Id")
            email=input("Enter a valid Email id: ")
if(a<3 and a==2):
    password=input("Enter a password: ")

    if len(password)>8 and not(password.islower() or password.isupper()):
        print("Strong Password")
        a+=1
    else: 
        print("WEAK PASSWORD, Your password should contain both uppercase and lowercase")
        password=input("Enter a password: ")