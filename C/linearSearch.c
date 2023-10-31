//This is a C program for Linear Search Algorithm
#include <stdio.h>

int main(){

    int n, data, i; //n = total number of elements of the array
    //data = the element the user searches for
    printf("Please, enter number of elements: ");
    scanf("%d",&n); //user input of total number/size of array elements
    int a[n]; //daclaration of array, given the total size(n)
    printf("Please, enter elements of the array: ");
    for(i=0;i<n;i++){// User input of the elements of the array
        scanf("%d",&a[i]);
    }
    printf("Please, enter element to be found: ");
    scanf("%d",&data); //user input of the data to be found
    for(i=0;i<n;i++){ //the number of iterations until the element the users searches for, is found
        if(a[i]==data){
            printf("Element %d found at index: %d",a[i],i);
            break; //the "break" statement is used to stop the "for" loop, when the desired element is found
            //if the users doen't type the 'break' statement, the loop will go on, even when the desired element is found
        }
    }
    if(i==n){ //this is the case when the whole array is search and the element the users searches for is not found in the array
    //The 'i==n' means that the user has reached the final element of the array
        printf("Element not found");
    }

    return 0;
}
