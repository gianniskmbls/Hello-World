# This Python program calculates the maximum and minimum intervals from a list of spaces provided by the user.
# A space is defined as a pair of start and end points, and the program finds the space or spaces with the longest
# and shortest lengths based on these intervals.
def maxminIntervals(spaces):
    # Initialize variables to keep track of the maximum and minimum intervals.
    max_interval = None
    min_interval = None

    # Initialize variables to keep track of the maximum and minimum interval lengths.
    max_length = float('-inf')  # Initialize to negative infinity
    min_length = float('inf')   # Initialize to positive infinity

    # Iterate through each space in the list of spaces.
    for space in spaces:
        # Calculate the length of the current space.
        space_length = space[1] - space[0]

        # Check if the current space has a longer length than the current maximum.
        if space_length > max_length:
            max_length = space_length
            max_interval = space

        # Check if the current space has a shorter length than the current minimum.
        if space_length < min_length:
            min_length = space_length
            min_interval = space

    # Return the maximum and minimum intervals.
    return {"max": max_interval, "min": min_interval}

# Get user input for the list of spaces
n = int(input("Enter the number of spaces: "))
spaces = []

for i in range(n):
    start = int(input(f"Enter the start of space {i + 1}: "))
    end = int(input(f"Enter the end of space {i + 1}: "))
    spaces.append([start, end])

# Call the function with the user-provided list of spaces
result = maxminIntervals(spaces)

# Print the list of spaces given by the user
print("List of spaces:", spaces)

# Print the maximum and minimum intervals
print("max =", result["max"], "and min =", result["min"])


