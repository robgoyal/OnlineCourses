/* Robin Goyal
   Given a person's name, print the initials 
*/

#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(void) {
    
    // Get user input for a string
    string s = get_string();
    int len = strlen(s);
    
    // Check to see if input string is not null
    if (s != NULL) {
        
        // Cheap condition to test if initial value is not a space char 
        if (s[0] != ' ') {
            printf("%c", toupper(s[0]));
        }
        
        /* Iterate through the first two characters to check for start of name
           and returns the uppercase output for the name
        */
        for (int i = 0; i < len - 1; i++) {
            if (s[i] == ' ' && s[i+1] != ' ') {
                printf("%c", toupper(s[i+1])); 
            }
            else {
                continue;
            }
        }
    }
    printf("\n");
}