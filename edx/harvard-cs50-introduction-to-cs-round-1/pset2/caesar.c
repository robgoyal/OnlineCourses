/* Robin Goyal
   Program to encrypt messages using Caesar's cipher
*/

#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>


int main(int argc, string argv[]) {
    
    // Check if number of args is 2
    if (argc != 2) {
        printf("Usage: ./caesar key");
        return 1;
    }
    
    // Convert 2nd arg to int 
    int key = atoi(argv[1]);
    
    printf("plaintext: ");
    string s = get_string();
    printf("ciphertext: ");
    
    /* Core logic to iterate through input string and 
       encrypt characters differently if uppercase or lowercase */
    for (int i = 0, len = strlen(s); i < len; i++) {
        if (isupper(s[i])) {
            printf("%c", (s[i] - 'A' + key) % 26 + 'A');
        }
        
        else if (islower(s[i])) {
            printf("%c", (s[i] - 'a' + key) % 26 + 'a');
        }
        
        else {
            printf("%c", s[i]);
        }
    }
    printf("\n");
    return 0;
    
}