# Identity Matrix Generator. Program to generate and display an identity matrix
# based on the number of 1s provided by the user.

# Get the number of 1s from the user
ones = int(input("Give number of 1s:"))

# Set the dimensions of the matrix
x = ones
y = ones

# Initialize a list of lists to represent the matrix
matrix = [''] * x

# Initialize the matrix with underscores
for k in range(x):
    matrix[k] = ['_'] * y

# Fill the matrix with zeros
for i in range(0, x):
    for j in range(0, y):
        matrix[i][j] = 0

# Set the diagonal elements to 1
for j in range(0, y):
    matrix[j][j] = 1

# Print the matrix
for i in range(0, x):
    for j in range(0, y):
        print(matrix[i][j], end=' ')
    print("")




