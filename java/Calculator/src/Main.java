//BASIC JAVA CALCULATOR
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        char operator;
        double number1, number2, result;

        // Create Scanner class object
        Scanner input = new Scanner(System.in);

        boolean validOperator = false;

        while (!validOperator) {
            // Ask user to enter operator
            System.out.print("Choose an operator (+, -, *, or /): ");
            operator = input.next().charAt(0);

            // Check if the entered operator is one of the valid operators
            if (operator == '+' || operator == '-' || operator == '*' || operator == '/') {
                validOperator = true; // Set flag to true to exit the loop
                // Ask user to enter numbers
                System.out.print("Enter first number: ");
                number1 = input.nextDouble();

                System.out.print("Enter second number: ");
                number2 = input.nextDouble();

                switch (operator) {
                    // performs addition between numbers
                    case '+':
                        result = number1 + number2;
                        System.out.println("The result is: " + number1 + " + " + number2 + " = " + result);
                        break;
                    // Performs subtraction between numbers
                    case '-':
                        result = number1 - number2;
                        System.out.println("The result is: " + number1 + " - " + number2 + " = " + result);
                        break;
                    // Performs multiplication between numbers
                    case '*':
                        result = number1 * number2;
                        System.out.println("The result is: " + number1 + " * " + number2 + " = " + result);
                        break;
                    // Performs division between numbers
                    // If denominator is zero (0), division cannot be performed
                    case '/':
                        if (number2 != 0) {
                            result = number1 / number2;
                            System.out.println("The result is: " + number1 + " / " + number2 + " = " + result);
                        } else {
                            System.out.println("Cannot perform division with zero (0) denominator");
                        }
                        break;
                }
            } else {
                // Display error message for invalid operator
                System.out.println("Error: Invalid operator. Please choose from +, -, *, or /.");
            }
        }
        input.close();
    }
}
