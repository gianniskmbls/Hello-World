# THIS IS A BANK APPLICATION WITH OOP CONCEPTS
# Creating the parent class 'Client' with its attributes and methods 
# The second class 'Bank' inherits from the parent class 'Client'

class Client():
    def __init__(self, first_name, last_name, age, gender, account_number):
        # Initializing the client with their details
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.account_number = account_number
    
    def display(self):
        # Printing the client's details
        print("Bank Client Details")
        print("===================")
        print("First Name: ", self.first_name)
        print("Last Name: ", self.last_name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)
        print("Account Number: ", self.account_number)

class Bank(Client):
    def __init__(self, first_name, last_name, age, gender, account_number):
        # Initializing the Bank class, inheriting from Client
        super().__init__(first_name, last_name, age, gender, account_number)
        # Starting with a balance of zero
        self.balance = 0
    
    def deposit(self, amount):
        # Adding money to the client's account
        self.amount = amount
        self.balance += self.amount
        print(f"Account balance updated successfully: {self.balance}€")

    def withdraw(self, amount):
        # Removing money from the client's account
        self.amount = amount
        if self.amount > self.balance:
            # Checking if there are enough funds
            print(f"Insufficient Funds - Balance Available: {self.balance}€")
        else:
            self.balance -= self.amount
            print(f"Account balance updated successfully: {self.balance}€")

    def check_balance(self):
        # Showing the client's details and current balance
        self.display()
        print(f"Current Account Balance: {self.balance}€")

def main():
    # Getting client information from user input
    first_name = input("Enter the client's first name: ")
    last_name = input("Enter the client's last name: ")
    age = int(input("Enter the client's age: "))
    gender = input("Enter the client's gender: ")
    account_number = int(input("Enter the client's account number: "))
    bank = Bank(first_name, last_name, age, gender, account_number)

    choice = 0
    # Looping until the user chooses to exit
    while choice != 4:
        print("=======YOUR PERSONAL BANK APPLICATION=======")
        print("1.Display client details and current balance")
        print("2.Deposit money in account")
        print("3.Withdraw money from account")
        print("4.Exit")
        choice = int(input("Please, select an option: "))

        if choice == 1:
            # Displaying client details and balance
            bank.check_balance()
        elif choice == 2:
            # Depositing money into the account
            amount = float(input("Enter the amount to deposit: €"))
            bank.deposit(amount)
        elif choice == 3:
            # Withdrawing money from the account
            amount = float(input("Enter the amount to withdraw: €"))
            bank.withdraw(amount)
        elif choice == 4:
            # Exiting the application
            print("Exiting application. Thank you!")
        else:
            # Handling invalid choices
            print("Invalid choice. Please try again.")
        print()

if __name__ == "__main__":
    main()
