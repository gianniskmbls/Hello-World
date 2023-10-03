//TEMPERATURE CONVERTER FROM CELSIUS TO FAHRENHEIT AND VICE VERSA
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // Create a Scanner object for user input
        Scanner input = new Scanner(System.in);

        // Display a menu for the user to choose the conversion type
        System.out.println("Temperature Converter");
        System.out.println("1. Celsius to Fahrenheit");
        System.out.println("2. Fahrenheit to Celsius");
        System.out.print("Enter your choice (1 or 2): ");

        // Read the user's choice
        int choice = input.nextInt();

        // Perform the chosen conversion
        if (choice == 1) {
            System.out.print("Enter temperature in Celsius: ");
            double celsius = input.nextDouble();
            double fahrenheit = (celsius * 9/5) + 32;
            System.out.println("Temperature in Fahrenheit: " + fahrenheit + " F");
        } else if (choice == 2) {
            System.out.print("Enter temperature in Fahrenheit: ");
            double fahrenheit = input.nextDouble();
            double celsius = (fahrenheit - 32) * 5/9;
            System.out.println("Temperature in Celsius: " + celsius + " C");
        } else {
            // Handle invalid choice
            System.out.println("Invalid choice. Please enter 1 for Celsius to Fahrenheit or 2 for Fahrenheit to Celsius.");
        }
        // Close the Scanner
        input.close();
    }
}

