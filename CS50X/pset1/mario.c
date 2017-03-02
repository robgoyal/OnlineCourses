/* Robin Goyal */
/* Prints a double half pyramid of specified height to console */

#include <stdio.h>
#include <cs50.h>

// Prototype of pyramid function
void pyramid(int n);

int main(void) 
{
    int height;
 
    // User input pyramid height between 0 and 23
    do {
        printf("Height: ");
        height = get_int();
    }
    while (height < 0 || height > 23);
    
    // Call pyramid function
    pyramid(height);
    
    return 0;
}

// Pyramid function abstracted from marin function
void pyramid(int n) {

    // Each row of pyramid of height n
    for (int i = 0; i < n; i++) {
        
        // Print the left pyramid spaces
        for (int j = 0; j < n - i-1; j++) {
            printf("%c", ' ');
        }
    
        // Print the left pyramid blocks
        for (int k = 0; k < i+1; k++) {
            printf("%c", '#');
        }    
        
        // Print the gaps
        printf("%c", ' ');
        printf("%c", ' ');
        
        // Print the right pyramid blocks
        for (int k = 0; k < i+1; k++) {
            printf("%c", '#');
        }
        
        // No need to print the right pyramid spaces
        printf("\n");
    }    
}