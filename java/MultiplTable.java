// JAVA MULTIPLICATION TABLE (1-10) PROGRAM OF A NUMBER PROVIDED BY THE USER
import java.util.Scanner;

public class MultiplTable {
  public static void main(String[] args) {
    // Create a Scanner object for user input
    Scanner scanner = new Scanner(System.in);

    // Prompt the user to enter a positive, non-zero integer for multiplication
    System.out.print("Enter a positive, non-zero integer for multiplication: ");
    
    // Read the user's input and store it in the 'num' variable
    int num = scanner.nextInt();

    // Display the message indicating the multiplication table is for 'num'
    System.out.println("Multiplication table of " + num + ":");

    // For loop to iterate from 1 to 10 for multipliers
    for (int j = 1; j <= 10; j++) {
      // Calculate the result of multiplying 'num' by 'j'
      int result = num * j;

      // Display the multiplication result in the format "num x j = result"
      System.out.println(num + " x " + j + " = " + result);
    }

    // Close the Scanner to release system resources
    scanner.close();
  }
}

