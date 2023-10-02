# Random Matrix Generation and Maximum Element Calculation
# Program generating a random matrix based on user input and then
# calculating and displaying the maximum element in the matrix.

import random  # Import the random module to generate random numbers
import numpy as np  # Import the numpy library for numerical operations
import array  # This import is not used in the provided code

# Get the number of rows and columns from the user
r = int(input("Enter the number of rows:"))
c = int(input("Enter the number of columns:"))

# Initialize an empty list to store the matrix
mtrx = []

# Generate the matrix entries using nested loops
for i in range(r):  # Loop through each row
    arr = []  # Initialize an empty list for the current row
    for j in range(c):  # Loop through each column in the row
        n = random.randint(0, 99)  # Generate a random integer between 0 and 99
        arr.append(n)  # Add the generated value to the current row list
    mtrx.append(arr)  # Add the row list to the matrix list

# Print the generated matrix
print("Generated Matrix:")
for i in range(r):
    for j in range(c):
        print(mtrx[i][j], end=" ")  # Print each element of the matrix
    print()  # Move to the next line after printing a row

# Calculate and print the maximum element using numpy
max_element = np.max(mtrx)  # Find the maximum element using numpy's max function
print("The maximum element is:", max_element)  # Print the maximum element
