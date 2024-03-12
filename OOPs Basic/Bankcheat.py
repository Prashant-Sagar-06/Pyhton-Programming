class bank:
    def __init__(self,account_holder,account_num,initial_balance = 0):
        self.account_holder = account_holder 
        self.account_number = account_num
        self.initial_balance = initial_balance     
    def deposit(self,add_money):
        self.initial_balance += add_money
        return f"Rs.{add_money} amount added successfully, and total amount = {self.initial_balance}"
    
    def withdraw(self,widrw_amnt):
        self.initial_balance -= widrw_amnt
        return f"After withdrawing , rest amount : {self.initial_balance}"
        
    def check_balance(self):
        print(f"Net balance : {self.initial_balance}") 


#SIR WALA CODE DAALNA H
class savingaccount(bank):
    def __init__(self,account_num,account_holder,balance = 0, interest_rate =0.02):  
        self.interest_rate = interest_rate
        super().__init__(account_num,account_holder,balance)   

    def add_interest(self):
        amount = self.balance *self.interest_rate
        self.balance +=amount

class CheckingAccount(bank):
    def __init__(self,account_num,account_holder,balance,overlimited_draft=100):
        super().__init__(account_num,account_holder,balance)
        self.overlimited_draft=overlimited_draft

    def withdraw(self,amount):
        if amount<= self.balance + self.overlimited_draft:
            self.balance-=amount
        else:
            print("insufficient balance")
accounts = []
count = 0            
while 1:
    print('''
    Welcome to GLA bank
    which bank you want to open
    1.Saving account
    2.checking Account 
    3. Current account 
    4. Exit      ''')         

    choice = int (input("ENTER  TEH CHOICE 1/2/3"))
    if choice==1:
        ac=savingaccount(100001,"ravi",100)
        while 1:
            print("Menu")
            print("1. Deposit")
            print("2. Withdraw")
            print("5. Display all acounts")
            ch=int (input("ENTER  TEH CHOICE 1/2/3"))
            if ch==1:
                accounts[count].deposit(1000)
        count+=1
    elif choice==4:
        break       

#if __name__=="__main__":
 #   savingaccount= savingaccount(12345,"ravi",100)
  #  CheckingAccount=CheckingAccount(1122333,"sagar",1200)


account_holder = input("Enter Account holder Name : ")   
account_number = eval(input("Enter account number : "))
amount = 0
c1 = bank(account_holder,account_number,amount)

while 1:
    print("""
    1. Deposit Amount 
    2. Withdraw Amount 
    3. Check Balance 
    4. Exit"""  )
    
    choice = input("Enter choice from [1-4] : ")   
    if choice == '1':
        add_amount = int(input("Enter amount to deposit : "))
        print(c1.deposit(add_amount))
    
    elif choice == '2':
        
        with_draw = int(input("Enter amount to withdraw : "))
        print(c1.withdraw(with_draw))
    elif choice == '3':
        c1.check_balance()
    elif choice == '4':
        print("Thank You! Exit the program")
        break
    else:
        print("Invalid choice! Please Enter the choice from 1-4")