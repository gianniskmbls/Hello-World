//JAVA FREQUENCY CALCULATOR OF INTEGER ARRAY ELEMENTS (INTEGERS 1-9)
public class Main {
    public static void main(String[] args) {
        int arr[] = {2, 3, 5, 6, 5, 6, 2, 3, 1, 7, 8, 5, 9, 1, 2, 1};

        // Iterate through numbers from 1 to 9
        for (int j = 1; j < 10; j++) {
            int count = 0;

            // Nested loop to count occurrences of the current number in the array
            for (int i = 0; i < arr.length; i++) {
                if (j == arr[i]) {
                    count++;
                }
            }

            // Print the element and its frequency
            System.out.print(j);
            System.out.print(": ");
            System.out.print(count);

            // Check if the element appears only once and adjust the output accordingly
            if (count == 1) {
                System.out.println(" time");
            }
            else {
                System.out.println(" times");
            }
        }
    }
}
