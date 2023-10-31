//Simple UI with menu options in C, using struct and link list
#include <stdio.h>
#include <string.h> //For string handling
#include <stdlib.h> //For malloc function

struct node{ //First, we need to create a data structure. In a linked list, we can have a set of data oof different type
//Each node includes the data plus the address of the next node it is connected with
    char fname[30];
    char lname[30];
    int age;
    char gender[20];
    char disease[20];
    int date;
    struct node *next; //Pointer with the address of the next node
};
struct node *head; //We must always have a pointer, with the  address of the first node. We usually name it 'head'
//NOTE: the node is not yet created, since we haven't allocated memory. We have only declared it
//At this point, 'head' points to no node. It's time to create the node (allocate memory)
void add(char fname[30], char lname[30], int age, char gender[20], char disease[20], int date){
    struct node *temp; //The '*temp' is the pointer to a new node. It is a temporary pointer and used every time we add a node
    temp = (struct node*)malloc(sizeof(struct node)); //The 'malloc' function returns a pointer to the starting address 
    //of the node memory block. The dynamic allocation
    strcpy(temp->fname, fname); //The 'strcpy' function is needed for string handling
    strcpy(temp->lname, lname);
    temp->age = age;
    strcpy(temp->gender, gender);
    strcpy(temp->disease, disease);
    temp->date = date;
    if(head == NULL){ //Case when 'head' points at no node address (no node to point at)
    head = temp; //The 'head' pointer becomes the 'temp' pointer
    temp->next = NULL; //The 'temp' points to no next node
    }
    else{
    temp->next = head; //There is already a node, whose 'temp' pointer becomes 'head'
    head = temp; //The 'head' pointer becomes the 'temp' pointer
    }
}
void deletefrombegin(){
    struct node *tmp;
    tmp = head;
    head = head->next;
    free(tmp);
}
void display(){
    struct node *r;
    r = head;
    if(r == NULL){
        return;
    }

    printf("----------------------------------------------------------------------------------------------------------\n");
    while(r!=NULL){
    printf("Full case profile: %s | %s | %d | %s | %s | %d\n",r->fname, r->lname, r->age, r->gender, r->disease, r->date);
    r = r->next;
    }
    printf("----------------------------------------------------------------------------------------------------------\n");
}
int count(){
    struct node *n;
    int cnt = 0;
    n = head;
    while(n != NULL){
        n = n->next;
        cnt++;
    }
    return cnt;
}
int main(){

int selection;
char fname[30], lname[30];
int age;
char gender[20];
char disease[20];
int date;

while(1){
    printf("Menu\n");
    printf("1.Add case\n");
    printf("2.Delete case\n");
    printf("3.Show number of cases\n");
    printf("4.Display full case profile\n");
    printf("5.Exit\n");
    printf("\nPlease, choose: ");
    scanf("%d",&selection);
    if(selection == 1){
        printf("Enter first name of case: ");
        scanf("%s",&fname);        
        printf("Enter last name of case: ");
        scanf("%s",&lname);
        printf("Enter age of case: ");
        scanf("%d",&age);
        printf("Enter gender of case: ");
        scanf("%s", &gender);        
        printf("Enter disease of case: ");
        scanf("%s",&disease);        
        printf("Enter record date: ");
        scanf("%d",&date);
        add(fname, lname, age, gender, disease, date);
    }
    else if(selection == 2){
        deletefrombegin();
    }
    else if(selection == 3){
        printf("%d\n",count());
    }
    else if(selection == 4){
        display();
    }
    else if(selection == 5){
        printf("You have exited successfully");
        return 0;
    }

}
return 0;
}
