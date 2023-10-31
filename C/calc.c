//Simple calculator using C programming language
#include <stdio.h>

int main(){

    char oper;
    double first, second;
    printf("Please, enter the operator (+,-,*,/): ");
    scanf("%c",&oper);

    printf("Please, enter two numbers: ");
    scanf("%lf %lf",&first,&second);

    switch(oper){
        case '+':
        printf("%.2lf + %.2lf = %.2lf",first,second,(first + second));
        break;

        case '-':
        printf("%.2lf - %.2lf = %.2lf",first,second,(first - second));
        break;

        case '*':
        printf("%.2lf * %.2lf = %.2lf",first,second,(first * second));
        break;

        case '/':
        if(second!=0){
          printf("%.2lf / %.2lf = %.2lf",first,second,(first / second));
        }
        else{
          printf("Division by zero cannot be performed");
        }
        break;

        default:
        printf("Invalid operator");
    }


    return 0;
}
