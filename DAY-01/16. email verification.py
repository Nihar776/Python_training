email=input("Enter an Email id: ")
if (email.endswith(".com") or email.endswith(".org")) and email.find("@")!=-1 :
    print("Valid Email Id")
else:
    print("Inalid Email Id")
    