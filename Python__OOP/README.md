# Introduction
The 'Python__OOP' folder contains Python applications that were implemented by using Object 
Oriented Programming concepts. Below is a brief description of each program:
## account.py - Personal Bank Application in Python
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


## cart.py - Shopping Cart Application in Python

This is a command-line shopping cart application built in Python using Object-Oriented Programming (OOP) concepts. The application allows users to add and remove items from a cart, view the contents of the cart, and calculate the total cost of the items in the cart.

### Features
- **Online Shop**: The `Shop` class represents the base class for the online shop, providing a foundation for the `Item` and `Cart` classes.
- **Item Management**: Create and manage items with attributes such as name, type, quantity, and cost.
- **Cart Operations**: Add items to the cart, remove specific quantities, view all items, and calculate the total cost of items in the cart.

### Classes and Methods
- **`Shop` Class**: Represents the online shop.
  - `display_shop_name()`: Displays the name of the shop.

- **`Item` Class**: Inherits from `Shop` and represents an item available in the shop.
  - `__init__(item_name, item_type, item_quantity, item_cost)`: Initializes an item with a name, type, quantity, and cost.
  - `display()`: Displays the details of the item.

- **`Cart` Class**: Inherits from `Shop` and represents a shopping cart.
  - `add_item(item)`: Adds an item to the cart or updates the quantity if the item already exists.
  - `remove_item(item_name, quantity)`: Removes a specified quantity of an item from the cart.
  - `display_cart()`: Displays the contents of the cart.
  - `total_cost()`: Calculates and displays the total cost of the items in the cart.

### Usage
1. **Start the application**: Run the script to begin interacting with the shopping cart.
2. **Choose an option from the menu**:
   - Add an item to the cart by specifying its name, type, quantity, and cost.
   - Remove a specified quantity of an item from the cart.
   - Display the current contents of the cart.
   - Calculate and display the total cost of the items in the cart.
   - Exit the application.

This application is a practical example of implementing a shopping cart system using OOP concepts in Python. It demonstrates how to manage items in a cart and perform common operations like adding, removing, and calculating costs.


