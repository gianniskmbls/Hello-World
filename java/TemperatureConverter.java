//SIMPLE TEMPERATURE CONVERTER IN JAVA
import java.util.Scanner;

public class TemperatureConverter {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int choice;
        do {
            // Display the menu
            System.out.println("Temperature Converter Menu:");
            System.out.println("1. Convert from Celsius to Fahrenheit");
            System.out.println("2. Convert from Fahrenheit to Celsius");
            System.out.println("3. Exit");
            System.out.print("Enter your choice: ");
            
            // Read user's choice
            choice = scanner.nextInt();
            
            // Perform the corresponding action based on user's choice
            switch (choice) {
                case 1:
                    convertCelsiusToFahrenheit();
                    break;
                case 2:
                    convertFahrenheitToCelsius();
                    break;
                case 3:
                    System.out.println("Exiting the program. Goodbye!");
                    break;
                default:
                    System.out.println("Invalid choice. Please enter 1, 2, or 3.");
            }
        } while (choice != 3);
        
        // Close the scanner when done to release resources
        scanner.close();
    }
    
    private static void convertCelsiusToFahrenheit() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter temperature in Celsius: ");
        double celsius = scanner.nextDouble();
        
        // Perform the Celsius to Fahrenheit conversion
        double fahrenheit = (celsius * 9/5) + 32;
        
        // Display the result
        System.out.println("Temperature in Fahrenheit: " + fahrenheit);
    }
    
    private static void convertFahrenheitToCelsius() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter temperature in Fahrenheit: ");
        double fahrenheit = scanner.nextDouble();
        
        // Perform the Fahrenheit to Celsius conversion
        double celsius = (fahrenheit - 32) * 5/9;
        
        // Display the result
        System.out.println("Temperature in Celsius: " + celsius);
    }
}
