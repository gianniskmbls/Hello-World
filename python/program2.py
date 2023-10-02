# Digital Root Calculation with Iterated Summing
# This code calculates the digital root of a given integer by performing iterative digit summing.
# It prompts the user to input a number, calculates the sum of its digits,
# then calculates the sum of digits of that sum (first sum), and iterates
# until a single-digit result (digital root) is obtained.
num = int(input("Please, enter a number:"))
def digit_sum(num):
    sum = 0   # Initialize the sum variable to store the sum of digits of the input number
    sum2 = 0  # Initialize the sum2 variable to store the sum of digits of the first sum
    sum3 = 0  # Initialize the sum3 variable to store the sum of digits of the second sum

    # Converting the integer into a string and iterating over each digit of the string
    for i in str(num):

        # Converting the string into integer, adding the digits' sum in every iteration
        sum += int(i)

    # Converting the integer into a string and iterating over each digit of the string
    for j in str(sum):

        # Converting the string into integer, adding the digits' sum in every iteration
        sum2 += int(j)

        # If 'sum2' is greater than 9, for example '10' we follow the same process as above
        if sum2 > 9:
            for k in str(sum2):  # Converting the integer into a string and iterating over each digit of the string
                sum3 += int(k)   # Adding the digits' sum in every iteration of the second sum
            return sum3  # Return the digital root of the second sum
    return sum2  # Return the digital root of the first sum if it's not greater than 9

print(digit_sum(num))


