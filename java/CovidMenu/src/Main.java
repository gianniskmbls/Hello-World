import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in); // Create a Scanner object for user input

        Menu menu = new Menu(); // Create an instance of the Menu class
        menu.runMenu(scanner); // Run the menu
    }

    static class Menu {

        boolean exit; // Flag to control the loop

        // ArrayList to store the cases (persons)
        ArrayList<Person> cases = new ArrayList<>();

        // Method to run the menu
        public void runMenu(Scanner scanner) {

            PrintHeader(); // Print the header
            while (!exit) { // Continue loop until exit flag is set to true
                PrintMenu(); // Print the menu options
                int choice = getInput(scanner); // Get user input for menu choice
                switch (choice) { // Switch case based on user choice
                    case 1:
                        addCase(scanner); // Add a case
                        break;
                    case 2:
                        deleteCase(scanner); // Delete a case
                        break;
                    case 3:
                        showNumberOfCases(); // Show number of cases
                        break;
                    case 4:
                        displayFullCaseProfile(); // Display full case profile
                        break;
                    case 5:
                        exit = true; // Exit the program
                        System.out.println("Exiting the program... Goodbye!");
                        break;
                }
            }
            scanner.close(); // Close the Scanner object
        }

        // Method to print the header
        private void PrintHeader() {

            System.out.println("========================================");
            System.out.println("     Welcome to the COVID Menu");
            System.out.println("========================================");
        }

        // Method to print the menu options
        private void PrintMenu() {

            System.out.println("\nPlease, choose an option:");
            System.out.println("----------------------------");
            System.out.println("1. Add a case");
            System.out.println("2. Delete a case");
            System.out.println("3. Show number of cases");
            System.out.println("4. Display full case profile");
            System.out.println("5. Exit");
        }

        // Method to get user input for menu choice
        private int getInput(Scanner scanner) {

            int choice = 0;

            // Validate user input
            while (choice < 1 || choice > 5) {
                try {
                    System.out.print("\nPlease, enter your choice: ");
                    String input = scanner.nextLine();

                    if (!input.matches("\\d+")) {
                        throw new NumberFormatException(); // throw exception if input is not a valid integer
                    }

                    choice = Integer.parseInt(input);

                    if (choice < 1 || choice > 5) {
                        throw new IllegalArgumentException(); // throw exception for choices outside the valid range
                    }
                } catch (NumberFormatException e) {
                    System.out.println("Invalid selection. Please enter a valid number between 1 and 5.");
                } catch (IllegalArgumentException e) {
                    System.out.println("Invalid selection. Please choose a number between 1 and 5.");
                }
            }

            return choice;
        }

        // Method to add a case (person)
        private void addCase(Scanner scanner) {
            System.out.println("\nEnter person's details:");
            System.out.print("First Name: ");
            String firstName = scanner.nextLine();
            System.out.print("Last Name: ");
            String lastName = scanner.nextLine();
            System.out.print("Age: ");
            int age = Integer.parseInt(scanner.nextLine());
            System.out.print("Gender: ");
            String gender = scanner.nextLine();
            System.out.print("Height: ");
            double height = Double.parseDouble(scanner.nextLine());
            System.out.print("Weight: ");
            double weight = Double.parseDouble(scanner.nextLine());

            // Create a new Person object and add it to the cases ArrayList
            Person person = new Person(firstName, lastName, age, gender, height, weight);
            cases.add(person);
            System.out.println("Case added successfully!");
        }

        // Method to delete a case (person)
        private void deleteCase(Scanner scanner) {
            System.out.print("\nEnter the index of the case to delete: ");
            int index = Integer.parseInt(scanner.nextLine());
            if (index >= 0 && index < cases.size()) {
                cases.remove(index);
                System.out.println("Case deleted successfully!");
            } else {
                System.out.println("Invalid index. No case found at index " + index);
            }
        }

        // Method to show the number of cases (persons)
        private void showNumberOfCases() {
            System.out.println("\nTotal number of cases: " + cases.size());
        }

        // Method to display the full case profile (person details)
        private void displayFullCaseProfile() {
            for (int i = 0; i < cases.size(); i++) {
                System.out.println("\nCase " + (i + 1) + " details:");
                System.out.println(cases.get(i));
            }
        }
    }

    // Class representing a Person
    static class Person {
        private String firstName;
        private String lastName;
        private int age;
        private String gender;
        private double height;
        private double weight;

        // Constructor to initialize Person object with details
        public Person(String firstName, String lastName, int age, String gender, double height, double weight) {
            this.firstName = firstName;
            this.lastName = lastName;
            this.age = age;
            this.gender = gender;
            this.height = height;
            this.weight = weight;
        }

        // Override toString method to display person details
        @Override
        public String toString() {
            return "Name: " + firstName + " " + lastName +
                    "\nAge: " + age +
                    "\nGender: " + gender +
                    "\nHeight: " + height +
                    "\nWeight: " + weight;
        }
    }
}
