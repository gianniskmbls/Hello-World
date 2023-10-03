//JAVA PROGRAM TO CHECK WHETHER A NUMBER IS PRIME OR NOT
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        // Prompt the user to enter a number
        System.out.print("Enter a number: ");
        int number = input.nextInt();

        // Check if the entered number is prime and display the result
        if (isPrime(number)) {
            System.out.println(number + " is a prime number.");
        } else {
            System.out.println(number + " is not a prime number.");
        }
        input.close();
    }
    // Function to check if a number is prime
    public static boolean isPrime(int num) {
        // If the number is less than or equal to 1, it's not prime
        if (num <= 1) {
            return false;
        }
        // If the number is 2 or 3, it's prime
        else if (num <= 3) {
            return true;
        }
        // If the number is divisible by 2 or 3, it's not prime
        else if (num % 2 == 0 || num % 3 == 0) {
            return false;
        } else {
            // Use a loop to check for divisors starting from 5
            int i = 5;
            while (i * i <= num) {
                // Check for divisors at i and i+2
                if (num % i == 0 || num % (i + 2) == 0) {
                    return false;
                }
                // Increment by 6 to skip multiples of 2 and 3
                i += 6;
            }
            // If no divisors are found, the number is prime
            return true;
        }
    }
}
