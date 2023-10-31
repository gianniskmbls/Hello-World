#include <stdio.h> // Include the standard input/output library for input and output functions.

int main() {
    char oper; // Declare a variable to store the operator character.
    double first, second; // Declare variables to store the two input numbers.

    // Prompt the user to enter an operator and read it into the 'oper' variable.
    printf("Please, enter the operator (+,-,*,/): ");
    scanf("%c", &oper);

    // Prompt the user to enter two numbers and read them into the 'first' and 'second' variables.
    printf("Please, enter two numbers: ");
    scanf("%lf %lf", &first, &second);

    // Use a switch statement to perform different operations based on the input operator.
    switch (oper) {
        case '+':
            // If the operator is '+', perform addition and print the result with two decimal places.
            printf("%.2lf + %.2lf = %.2lf", first, second, (first + second));
            break;

        case '-':
            // If the operator is '-', perform subtraction and print the result with two decimal places.
            printf("%.2lf - %.2lf = %.2lf", first, second, (first - second));
            break;

        case '*':
            // If the operator is '*', perform multiplication and print the result with two decimal places.
            printf("%.2lf * %.2lf = %.2lf", first, second, (first * second));
            break;

        case '/':
            // If the operator is '/', check if the second number is not zero.
            // If it's not zero, perform division and print the result with two decimal places.
            // If the second number is zero, print a message indicating division by zero is not allowed.
            if (second != 0) {
                printf("%.2lf / %.2lf = %.2lf", first, second, (first / second));
            } else {
                printf("Division by zero cannot be performed");
            }
            break;

        default:
            // If the operator is not one of the recognized operators, print an error message.
            printf("Invalid operator");
    }

    return 0; // Return 0 to indicate successful program execution.
}
