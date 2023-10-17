// C PROGRAM TO CHECK WHETHER AN INTEGER IS POSITIVE, NEGATIVE OR EQUAL TO ZERO
// THIS PROGRAM ALSO CHECKS WHETHER THIS INTEGER IS EVEN OR ODD
#include <stdio.h>
#include <stdbool.h> // Include the standard library for boolean values

int main() {
    int n;
    printf("Please, enter an integer: ");

    if (scanf("%d", &n) != 1) {
        printf("Invalid input. Please enter an integer.\n");
        return false; // Use symbolic constant 'false' to indicate an error
    }

    if (n > 0) {
        printf("The value of the number is positive");
    } else if (n < 0) {
        printf("The value of the number is negative");
    } else {
        printf("The value of the number is equal to zero");
    }

    // Check if the number is even or odd
    if (n % 2 == 0) {
        printf("\nThe number is even.\n");
    } else {
        printf("\nThe number is odd.\n");
    }

    return true; // Use symbolic constant 'true' to indicate successful program execution
}

