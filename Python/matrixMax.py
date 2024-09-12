# Random Matrix Generator with Maximum Element Finder.
# Python program which generates a random matrix based on user input and then
# calculates and displays the maximum element in the matrix.

import random

# Function to generate a random matrix of given size (rows x cols)
def generate_random_matrix(rows, cols):
    matrix = []
    for _ in range(rows):
        # Create a row with random integers in the range [1, 100]. You can adjust this range as needed.
        row = [random.randint(1, 100) for _ in range(cols)]
        matrix.append(row)
    return matrix


# Function to find the maximum element in the matrix
def find_max_element(matrix):
    max_element = matrix[0][0]
    for row in matrix:
        for element in row:
            if element > max_element:
                max_element = element
    return max_element


# Main function to handle user input and display results
def main():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    # Check if the user provided valid input (rows and cols greater than zero)
    if rows <= 0 or cols <= 0:
        print("Rows and columns must be greater than zero.")
        return

    # Generate a random matrix
    matrix = generate_random_matrix(rows, cols)

    print("Generated Matrix:")
    for row in matrix:
        print(row)

    # Find the maximum element in the matrix
    max_element = find_max_element(matrix)
    print(f"The maximum element in the matrix is: {max_element}")


# Entry point of the program
if __name__ == "__main__":
    main()
