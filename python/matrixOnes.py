# Identity Matrix Generator with Error Handling
# This Python program generates and displays an identity matrix.
# An identity matrix is a square matrix where all diagonal elements are '1's,
# and all other elements are '0's. The user specifies the number of '1's in the matrix.

try:
    # Get the number of '1's from the user
    ones = int(input("Give the number of '1's:"))

    # Check if the input is a positive integer
    if ones <= 0:
        raise ValueError("Input must be a positive integer")

    # Set the dimensions of the matrix
    x = ones  # The number of rows is equal to the number of '1's
    y = ones  # The number of columns is also equal to the number of '1's

    # Initialize a list of lists to represent the matrix, initially filled with '0's
    matrix = [['0' for _ in range(x)] for _ in range(y)]

    # Set the diagonal elements of the matrix to '1's
    for j in range(y):
        matrix[j][j] = '1'

    # Print the matrix
    for i in range(x):
        for j in range(y):
            print(matrix[i][j], end=' ')  # Print each element of the matrix
        print("")  # Move to the next row for a clean display

except ValueError as e:
    print(f"Error: {e}. Please enter a valid positive integer for the number of '1's.")
    print("Example: Enter '3' for a 3x3 identity matrix.")
