//MULTIPLICATION TABLE FROM 1 TO 10
public class Main {
    public static void main(String[] args) {
        // Outer loop: Iterates through numbers from 1 to 10.
        for (int i = 1; i <= 10; i++) {
            // Print a header indicating the current number's multiplication table.
            System.out.println("Multiplication table of: " + i);

            // Inner loop: Generates the multiplication table for the current number.
            for (int j = 1; j <= 10; j++) {
                // Calculate the product of i and j.
                int b = i * j;
                // Display the multiplication expression and result.
                System.out.println(i + " x " + j +  "= " + b );
            }
            // Add a blank line to separate each multiplication table.
            System.out.println("");
        }
    }
}