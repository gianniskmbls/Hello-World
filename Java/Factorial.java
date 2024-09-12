import java.util.Scanner;

public class Factorial {
  public static void main(String[] args) {
   
    // Create a Scanner object for reading user input
    Scanner scan = new Scanner(System.in);

    // Declare and initialize variables
    int fact = 1; // Initialize the factorial to 1 (the base case)

    // Display an empty line for better output formatting
    System.out.println();

    // Prompt the user to enter a positive integer
    System.out.print("Please, enter a positive integer: ");

    // Read the number for which we want to calculate the factorial from the user
    int num = scan.nextInt();

    // Calculate the factorial of the given number using a for loop
    for (int i = 1; i <= num; i++) {
      // Multiply the current factorial by 'i' in each iteration
      fact = fact * i;
    }

    // Print the factorial of the given number
    System.out.println("Factorial of " + num + " is: " + fact);

    // Close the Scanner to release resources
    scan.close();
  }
}
