# Introduction
The 'Python__OOP' folder contains Python applications that were implemented by using Object 
Oriented Programming concepts. Below is a brief description of each program:
## account.py
## Personal Bank Application in Python
This is a simple command-line bank application built in Python using Object-Oriented Programming (OOP) principles. The application enables users to manage a bank account by creating a client profile, depositing and withdrawing funds, and viewing account details and the current balance.
### Features
-Client Management: Create a new client with basic details such as first name, last name, age, gender, and account number.
-Deposit Funds: Add money to the client's account.
-Withdraw Funds: Withdraw money from the account, with a check for insufficient funds.
-Account Overview: Display the client's details along with the current account balance.
### Classes and Methods
-Client Class: Stores client information (name, age, gender, account number).
  -display(): Prints the client’s details.
-Bank Class: Inherits from Client, managing bank-specific functions.
  -deposit(amount): Deposits a specified amount into the account.
  -withdraw(amount): Withdraws a specified amount from the account, ensuring sufficient funds.
  -check_balance(): Displays the client’s details and the current balance.
### Usage
 1. Start the application: Run the script and input client details when prompted.
 2. Choose an option:
  -Display client details and current balance.
  -Deposit money into the account.
  -Withdraw money from the account.
  -Exit the application.

This application is an excellent example of how to implement basic banking operations using OOP concepts in Python.
