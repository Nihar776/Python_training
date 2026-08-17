password=input("Enter a password to check its strength: ")

if len(password)>8 and not(password==password.lower() or password==password.upper()):
    print("Strong Password")
else: 
    print("WEAK PASSWORD, Your password should contain both uppercase and lowercase")