//BUBBLE SORT SORTING ALGORITHM
import java.util.Scanner; // Import Scanner class for user input

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in); // Create a Scanner object for user input

        System.out.print("Enter the number of elements in the array:");
        int n = scanner.nextInt(); // Read the number of elements from the user

        int arr[] = new int[n]; // Create an array to store the elements

        System.out.println("Enter the elements of the array:");
        for (int i = 0; i < n; i++) {
            arr[i] = scanner.nextInt(); // Read each element from the user
        }

        scanner.close(); // Close the scanner

        // Printing array elements in one line
        System.out.println("Original array:");
        for (int i = 0; i < n; i++) {
            int a = arr[i];
            System.out.print(a + " ");
        }
        System.out.println("\n");

        // Bubble Sort Algorithm
        for (int i = 0; i < n; i++) {
            for (int j = 1; j < (n - i); j++) {
                // If left number is greater than the number in the right:
                if (arr[j - 1] > arr[j]) {
                    // Swap the numbers
                    int tmp = arr[j - 1];
                    arr[j - 1] = arr[j];
                    arr[j] = tmp;
                }
            }

            // Print array after each pass
            System.out.println("Array after pass " + (i + 1) + ":");
            for (int x = 0; x < n; x++) {
                int a = arr[x];
                System.out.print(a + " ");
            }
            System.out.println("\n");
        }

        // Print sorted array
        System.out.println("Sorted array:");
        for (int i = 0; i < n; i++) {
            int a = arr[i];
            System.out.print(a + " ");
        }
        System.out.println("\n");
    }
}
