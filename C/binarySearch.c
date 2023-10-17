// THIS IS A C PROGRAM FOR BINARY SEARCH ALGORITHM
// THE ARRAY MUST BE SORTED IN AN ASCENDING ORDER
#include <stdio.h>

// Binary search function that searches for 'data' in array 'a' between indices 'low' and 'high'
int binarySearch(int a[], int data, int low, int high) {
  // Repeat until the pointers 'low' and 'high' meet each other
  while (low <= high) {
    // Calculate the middle index
    int mid = low + (high - low) / 2;

    // If the middle element is equal to 'data', return its index
    if (a[mid] == data)
      return mid;

    // If the middle element is less than 'data', update 'low' to search the right half
    if (a[mid] < data)
      low = mid + 1;

    // If the middle element is greater than 'data', update 'high' to search the left half
    else
      high = mid - 1;
  }

  // If 'data' is not found in the array, return -1
  return -1;
}

int main(void) {
    int i, n, data;

    // Prompt the user to enter the number of elements in the array
    printf("Please, enter the number of elements: ");
    scanf("%d", &n);

    // Declare an array 'a' with a fixed size (adjust as needed)
    int a[100]; // Fixed-size array with a size of 100

    // Prompt the user to enter the elements of the array
    printf("Please, enter elements of the array: ");
    for (i = 0; i < n; i++) {
        // User input of the elements of the array
        scanf("%d", &a[i]);
    }

    // Prompt the user to enter the element to be found
    printf("Please, enter the element to be found: ");
    scanf("%d", &data);

    // Call the binarySearch function to search for 'data' in array 'a'
    int result = binarySearch(a, data, 0, n - 1);

    // Check if the result is -1, indicating 'data' was not found
    if (result == -1)
     printf("Element not found");
   else
     // If 'data' was found, print its index
     printf("Element is found at index %d", result);

  return 0;
}


