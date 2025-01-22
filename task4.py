# python task 4th 

class BankAccount:
    def __init__(self):
        self.__balance = 0
        
    def deposit(self,amount):
        if amount > 0:
            self.__balance +=amount
            print("Balance after deposit: ",self.__balance)
        else:
            print("invalid deposit amount ")
            
    def withdraw(self,amount):
        if amount > 0:
            if self.__balance >amount:
                self.__balance -=amount
                print("Balance after withdrawal: ",self.__balance)
            else:
                print("insufficient balance")
                
        else:
            print("enter valid withdrawal amount")
            
    def get_balance(self):
        print("current balance:", self.__balance)
        
    
account = BankAccount()
account.deposit(1000)
account.withdraw(200)
account.get_balance()
