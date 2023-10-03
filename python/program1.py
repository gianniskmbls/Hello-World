# Max and Min Interval Calculator.
# Program of a function which takes a list of spaces as an input
# and returns the space or spaces with the longest and shortest length.
# For example: maxminIntervals ( [[1,2], [6, 10], [10, 15] ] ) returns max=[10, 15] and min=[1,2],
# maxminIntervals ( [[1,4], [5, 10], [3, 5] ] ) returns max=[5, 10] and min=[3,5].
def minmaxIntervals():
    lst2 = []  # Initialize a list to store intervals

    # Get the number of intervals from the user
    size2 = int(input("Enter the number of intervals: "))

    # Loop to input intervals and their elements
    for i in range(size2):
        lst3 = []  # Initialize a list to store elements within an interval

        # Get the size of the current interval from the user
        size3 = int(input(f"Enter the size of interval {i + 1}: "))

        # Loop to input elements for the current interval
        for j in range(size3):
            element = int(input(f"Enter element {j + 1} for interval {i + 1}: "))
            lst3.append(element)  # Add the element to the current interval

        lst2.append(lst3)  # Add the current interval to the list of intervals

    interval_min_max = []  # Initialize a list to store tuples of interval min and max

    # Loop to calculate min and max for each interval
    for interval in lst2:
        interval_max = max(interval)  # Calculate max for the current interval
        interval_min = min(interval)  # Calculate min for the current interval
        interval_min_max.append((interval_min, interval_max))  # Add tuple to list

    # Calculate overall max and min based on interval_min_max list
    overall_max = max(interval_min_max, key=lambda x: x[1])  # Calculate overall max
    overall_min = min(interval_min_max, key=lambda x: x[0])  # Calculate overall min

    return interval_min_max, overall_max, overall_min  # Return results

# Call the function and print the results
print(minmaxIntervals())
