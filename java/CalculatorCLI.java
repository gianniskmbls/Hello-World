//SIMPLE COMMAND LINE CALCULATOR IN JAVA
import java.util.Scanner;

public class CalculatorCLI {

    public static void main(String[] args) {
        // Create a Scanner object to read input from the user
        Scanner scanner = new Scanner(System.in);

        System.out.println("Simple CLI Calculator");
        System.out.println("Supported Operations: +, -, *, /");
        System.out.println("Enter your calculation (e.g., 2 + 3):");

        // Read the user's input as a string
        String input = scanner.nextLine();

        // Split the input string into operands and operator
        String[] parts = input.split(" ");
        if (parts.length != 3) {
            System.out.println("Invalid input. Please use the format: operand1 operator operand2");
            return;
        }

	
        // Extract operands and operator
	/*The expression parts[1].charAt(0) is used to extract the first character (character at index 0) from the string located at parts[1]. 
	In Java, strings are indexed starting from 0, so the first character of a string is at index 0, the second character at index 1, and so on.*/
        double operand1 = Double.parseDouble(parts[0]);
        char operator = parts[1].charAt(0); // We assume the operator is a single character.
        double operand2 = Double.parseDouble(parts[2]);

        // Perform the calculation based on the operator
        double result = 0.0;

        switch (operator) {
            case '+':
                result = operand1 + operand2;
                break;
            case '-':
                result = operand1 - operand2;
                break;
            case '*':
                result = operand1 * operand2;
                break;
            case '/':
                if (operand2 != 0) {
                    result = operand1 / operand2;
                } else {
                    System.out.println("Division by zero is not allowed.");
                    return;
                }
                break;
            default:
                System.out.println("Invalid operator. Please use one of: +, -, *, /");
                return;
        }

        // Display the result
        System.out.println("Result: " + result);

        // Close the scanner, in order to release resources properly
        scanner.close();
    }
}
