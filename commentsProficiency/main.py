#the class for a bank account
class BankAccount:
    def __init__(self, account_number, balance=0):
        #sets the current account_number
        self.account_number = account_number
        #sets the current balance
        self.balance = balance

    def deposit(self, amount):
        #checks if there is a deposit
        if amount > 0:
            #adds the deposit to the balance of the bank account
            self.balance += amount
            return True
        #if there isn't a deposit, return false
        return False

    def withdraw(self, amount):
        #checks if there is a withdrawal
        if 0 < amount <= self.balance:
            #removes the withdrawal from the account balance 
            self.balance -= amount
            return True
        #if there isn't a withdrawal, return false
        return False

    def get_balance(self):
        #gives the current account balance
        return self.balance

def create_account():
    #asks for the number for the new account
    account_number = input("Enter account number: ")
    #asks for the balance for the new account
    initial_balance = float(input("Enter initial balance: "))
    #returns an instance of BankAccount with the number of the account and the balance of the account
    return BankAccount(account_number, initial_balance)

def main():
    #array of all accounts
    accounts = {}
    while True:
        #user instructions
        print("\n1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        #ask for what the user wants to do
        choice = input("Enter your choice (1-5): ")
        #if user want to make a new account:
        if choice == '1':
            #runs create_account function
            account = create_account()
            #puts the account number in the accounts database
            accounts[account.account_number] = account
            #prints that the account with the specific account number has been created
            print(f"Account {account.account_number} created successfully!")
        #if user wants to deposit, withdraw, or check their balance:
        elif choice in ['2', '3', '4']:
            #user enters specific account number
            account_number = input("Enter account number: ")
            #checks if the account number is in the accounts database
            if account_number in accounts:
                #if it is, set the variable "account" to the account number we are 
                #accessing for uses in the deposits, withdrawals, and checking account balance  
                account = accounts[account_number]
                #if the user want to deposit:
                if choice == '2':
                    #asks user how much they want to deposit
                    amount = float(input("Enter deposit amount: "))
                    #if the amount the user wants to deposit is positive:
                    if account.deposit(amount):
                        #prints that the deposit was successful
                        print(f"Deposited ${amount:.2f} successfully!")
                    #if the amount that the user wants to deposit is not positive:
                    else:
                        #prints that the deposit was not successful
                        print("Invalid deposit amount.")
                #if the user want to withdraw:                
                elif choice == '3':
                    #asks user how much they want to withdraw
                    amount = float(input("Enter withdrawal amount: "))\
                    #if the amount the user wants to withdraw is positive:
                    if account.withdraw(amount):
                        #prints that the withdrawal was successful
                        print(f"Withdrawn ${amount:.2f} successfully!")
                    #if the amount the user wants to withdraw is negative:
                    else:
                        #prints that the withdrawal was not successful
                        print("Invalid withdrawal amount or insufficient funds.")
                #if the user didn't input 2 or 3 but their input fits into the category of being 2,3, or 4, then  
                #their input must be 4, therefore running this print statement which prints the account balance:
                else:
                    #prints current account balance
                    print(f"Current balance: ${account.get_balance():.2f}")
            #if the account number is not found in the accounts database: 
            else:
                #prints that the account is not found
                print("Account not found.")
        #if the choice is 5 then they are wanting to exit which runs this:
        elif choice == '5':
            #leaving statement
            print("Thank you for using our banking system. Goodbye!")
            #breaks the loop of running the user inputs
            break
        #if the user choice doesn't input 1,2,3,4, or 5:
        else:
            #prints the number isn't valid
            print("Invalid choice. Please try again.")
#checks if the name of the file is main:
if __name__ == "__main__":
    #run the main function
    main()