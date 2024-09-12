# Digital Root Calculator with Iterated Summing.
# This  program calculates the digital root of a given integer using iterative digit summing.
# The digital root is the repeated sum of the digits of a number until a single-digit result is obtained.

# Define a function to calculate the digital root using iterative digit summing
def digital_root(n):
    while n >= 10:  # Continue the loop as long as the number has two or more digits
        n = sum(int(digit) for digit in str(n))  # Calculate the sum of digits of the number
    return n  # Return the single-digit digital root


# Define the main function to take user input and calculate the digital root
def main():
    try:
        # Prompt the user to enter an integer and convert it to an integer
        num = int(input("Enter an integer: "))

        # Check if the entered number is negative
        if num < 0:
            print("Please enter a positive integer.")
        else:
            # Calculate the digital root of the entered integer
            result = digital_root(num)
            # Display the result
            print(f"The digital root of {num} is {result}.")
    except ValueError:
        # Handle the ValueError exception if the input is not a valid integer
        print("Invalid input. Please enter a valid integer.")


# Check if the script is run as the main program
if __name__ == "__main__":
    # Call the main function
    main()
