//BUBBLESORT SORTING ALGORITHM
public class Main {
    public static void main(String[] args) {
        //Printing array elements in one line
        int arr[] = {98, 44, 55, 11, 77, 33, 99, 22, 12, 92, 72, 10};
        int n = arr.length;
        for (int i = 0; i < n; i++) {
            int a = arr[i];
            System.out.print(a + " ");
        }
        System.out.println(" ");
        System.out.println(" ");
        //Bring minimum number in index zero (0)
        for(int i =0;i < n;i++){
            for(int j = 1; j < (n-i);j++){
                //If left number is smaller than the number in the right:
                if(arr[j-1]>arr[j]){
                    //Change number position: biggest number goes right
                    int tmp = 0;
                    tmp = arr[j-1];
                    arr[j-1] = arr[j];
                    arr[j] = tmp;
                }
            }
            //Print consecutive algorithm steps
            for (int x = 0; x < n; x++) {
                int a = arr[x];
                System.out.print(a + " ");
            }
            System.out.println(" ");

        }
        System.out.println(" ");
        //Print again, array elements in one line
        for (int i = 0; i < n; i++) {
            int a = arr[i];
            System.out.print(a + " ");
        }
        System.out.println(" ");
    }
}