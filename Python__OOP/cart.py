# THIS IS A SHOPPING CART APPLICATION WITH OOP CONCEPTS
# Defining a base class Shop representing the online shop
# Class Shop is parent class of Item and Cart classes

class Shop:
    def __init__(self):
        self.name = "Your Online Shop"  # Initializing the shop with a name

    def display_shop_name(self):
        print(f"Welcome to {self.name}")  # Displaying the shop name

# Defining a class Item which inherits from Shop and represents an item in the shop
class Item(Shop):
    def __init__(self, item_name, item_type, item_quantity, item_cost):
        super().__init__()  # Calling the constructor of the parent class Shop
        self.item_name = item_name          # Name of the item
        self.item_type = item_type          # Type of the item
        self.item_quantity = item_quantity  # Quantity of the item
        self.item_cost = item_cost          # Cost of the item

    def display(self):
        # Displaying the item's details
        print("Item Name: ", self.item_name)
        print("Item Type: ", self.item_type)
        print("Item Quantity: ", self.item_quantity)
        print("Item Price: €", self.item_cost)

# Defining a class Cart which inherits from Shop and represents a shopping cart
class Cart(Shop):
    def __init__(self):
        super().__init__()  # Calling the constructor of the parent class Shop
        self.items = []  # Initializing an empty list to store items

    def add_item(self, item):
        # Add an item to the cart, or update quantity if it already exists
        for cart_item in self.items:
            if cart_item.item_name == item.item_name:  # Checking if the item is already in the cart
                cart_item.item_quantity += item.item_quantity  # Updating the quantity
                print(f"Added {item.item_quantity} more of {item.item_name} to the cart.")
                return
        self.items.append(item)  # Adding the new item to the cart
        print(f"Added {item.item_name} to the cart.")

    def remove_item(self, item_name, quantity=1):
        # Removing a specified quantity of an item from the cart
        for item in self.items:
            if item.item_name == item_name:  # Finding the item in the cart
                if item.item_quantity > quantity:  # If there is enough quantity, reduce it
                    item.item_quantity -= quantity
                    print(f"Removed {quantity} of {item_name} from the cart. Remaining quantity: {item.item_quantity}")
                elif item.item_quantity == quantity:  # If exact quantity, remove the item
                    self.items.remove(item)
                    print(f"Removed {item_name} from the cart.")
                else:
                    print(f"Cannot remove {quantity} of {item_name}. Only {item.item_quantity} in cart.")  # Not enough quantity
                return
        else:
            print(f"Item {item_name} not found in the cart.")  # Item not in cart

    def display_cart(self):
        # Displaying the contents of the cart
        if not self.items:
            print("The cart is empty.")  # Cart is empty
        else:
            print("Shopping Cart Contents")
            print("======================")
            for item in self.items:
                item.display()  # Displaying each item's details
                print("----------------------")

    def total_cost(self):
        # Calculating and displaying the total cost of items in the cart
        total = sum(item.item_cost * item.item_quantity for item in self.items)
        print(f"Total Cart Cost: € {total:.2f}")

# Defining the main menu function to interact with the user
def main():
    cart = Cart()  # Creating a new shopping cart instance
    cart.display_shop_name()  # Displaying the shop name

    while True:
        # Displaying menu options
        print("\n========== MENU ==========")
        print("1. Add item to cart")
        print("2. Remove item from cart")
        print("3. Display cart contents")
        print("4. Show total cost")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")  # Get user input for menu choice

        if choice == '1':
            # Adding item to cart
            item_name = input("Enter item name: ")
            item_type = input("Enter item type: ")
            item_quantity = int(input("Enter item quantity: "))
            item_cost = float(input("Enter item cost: "))
            item = Item(item_name, item_type, item_quantity, item_cost)  # Creating a new item
            cart.add_item(item)  # Adding the item to the cart
        elif choice == '2':
            # Removing item from cart
            item_name = input("Enter the name of the item to remove: ")
            quantity = int(input("Enter the quantity to remove: "))
            cart.remove_item(item_name, quantity)  # Removing the specified quantity of the item from the cart
        elif choice == '3':
            # Displaying cart contents
            cart.display_cart()  # Show the cart's contents
        elif choice == '4':
            # Show total cost of cart
            cart.total_cost()  # Displaying the total cost of items in the cart
        elif choice == '5':
            # Exiting the program
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")  # Invalid input

# Run the main menu function if this script is executed directly
if __name__ == "__main__":
    main()
