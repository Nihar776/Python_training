class BankAccount:
    def __init__(self,accNo,password):
        self.accNo=accNo
        self.__password=password

    def __showPass(self):
        # print(self.__password)
        return self.__password
    
    def __changePass(self,oldPass):
        
        if oldPass==self.__showPass():
            self.__password=input("Enter new password: ")
            print("Your new password is: ",self.__showPass())
            return True
        else:
            print("Access Denied: Wrong password.")
            return False

    def changePassword(self):
        not_done=True
        while(not_done):
            response=input("Do you want to change your password(y/n): ")
            if response=='y':
                oldPass=input("Enter your old password: ")
                not_done=not(self.__changePass(oldPass))
            elif response=='n':
                not_done=False
                pass
            else:
                print("Invalid input")

a=BankAccount(5185165985631252,'ABC123')
a.changePassword()