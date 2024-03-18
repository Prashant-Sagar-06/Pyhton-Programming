class BankAccount:
    def __init__(self,account_number,account_holder,initial_balance=0):
        self.account_holder=account_holder
        self.account_number=account_number
        self.initial_balance=initial_balance
    def deposit(self,add_money):
        self.initial_balance+= add_money
        return f" Rs. {add_money}Amount added Successfully Your balance is :- {self.initial_balance}"
    def withdraw(self, with_draw):
        if with_draw <= self.initial_balance:
            self.initial_balance -= with_draw
            return f"Rs. {with_draw} withdrawn. New balance: Rs. {self.initial_balance}"
        else:
            return "Insufficient funds"

class SavingAccount(BankAccount):
    def __init__(self, account_number, account_holder, initial_balance,interestrate=0.2):
        super().__init__(account_number, account_holder,initial_balance)
        self.interestrate=interestrate     
    def add_interest(self):
        amount = self.initial_balance *self.interestrate
        self.initial_balance +=amount
        return f"Interest calculated. New balance: Rs. {self.initial_balance}"

#Main code
account_holder = input("Enter Account holder Name : ")   
account_number = eval(input("Enter account number : "))
amount = 5000
user1 = SavingAccount(account_holder,account_number,amount)


while 1:
    print("""
    1. Deposit Amount 
    2. Withdraw Amount  
    3. Exit"""  )
    
    choice = input("Enter choice from [1-3] : ")   
    if choice == '1':
        add_amount = int(input("Enter amount to deposit : "))
        print(user1.deposit(add_amount))
    
    elif choice == '2':
        
        with_draw = int(input("Enter amount to withdraw : "))
        print(user1.withdraw(with_draw))
        
    elif choice=="3":
        print("Exited successfully:")
        print(user1.add_interest())
    else:
        print("Invalid choice! Please Enter the choice from 1-3") 
        