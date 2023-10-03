//BASIC JAVA CALCULATOR
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        char operator;
        Double number1, number2, result;

        //Create Scanner class object
        Scanner input = new Scanner(System.in);

        //Ask user to enter operator
        System.out.print("Choose an operator (+, -, *, or /): ");
        operator = input.next().charAt(0);

        // Ask user to enter numbers
        System.out.print("Enter first number: ");
        number1 = input.nextDouble();

        System.out.print("Enter second number: ");
        number2 = input.nextDouble();

        switch (operator) {

            //performs addition between numbers
            case '+':
                result = number1 + number2;
                System.out.println("The result is: " + number1 + " + " + number2 + " = " + result);
                break;

            //Performs subtraction between numbers
            case '-':
                result = number1 - number2;
                System.out.println("The result is: " + number1 + " - " + number2 + " = " + result);
                break;

            //Performs multiplication between numbers
            case '*':
                result = number1 * number2;
                System.out.println("The result is: " + number1 + " * " + number2 + " = " + result);
                break;

            //Performs division between numbers
            //If denominator is zero (0), division cannot be performed
            case '/':
                result = number1 / number2;
                if(number2 == 0){
                    System.out.println("Cannot perform division with zero (0) denominator");
                }
                else{
                    System.out.println("The result is: " + number1 + " / " + number2 + " = " + result);
                }
                break;
            //When pressing an invalid key-option, error message appears
            default:
                System.out.println("Error: Invalid operator");
                break;
        }
        input.close();
    }
}