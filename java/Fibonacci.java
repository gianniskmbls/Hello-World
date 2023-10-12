import java.util.Scanner;

public class Fibonacci {
  public static void main(String[] args) {

    // Create a Scanner object for reading user input
    Scanner input = new Scanner(System.in);

    // Initialize the first two Fibonacci numbers
    int previous = 0;
    int current = 1;
    int next = 0; // Variable to store the sum of "previous" and "current"

    // Print the initial values of "previous" and "current"
    System.out.print(previous);
    System.out.println("...: Initial sequence value ");
    System.out.print(current);
    System.out.println("...: Initial sequence value\n");

    // Prompt the user to enter a positive integer
    System.out.print("Please, enter a positive integer: ");

    // Read the number of Fibonacci numbers to generate from the user
    int num = input.nextInt();

    System.out.print("\n");

    // Generate the Fibonacci sequence for 'num' iterations
    for (int i = 1; i <= num; i++) {
      // Calculate the next Fibonacci number as the sum of the previous two
      next = previous + current;

      // Print the current Fibonacci number
      System.out.print(next);

      // Print a message indicating the sum of "previous" and "current"
      System.out.print("...: Sum: ");
      System.out.print(previous); // Print the value of "previous"
      System.out.print(" + ");
      System.out.println(current); // Print the value of "current"

      // Update "previous" and "current" for the next iteration
      previous = current;
      current = next;
    }

    // Close the Scanner to release resources
    input.close();
  }
}
