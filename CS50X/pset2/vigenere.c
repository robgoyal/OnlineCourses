/* Robin Goyal 
   Program which encrypts messages using Vigenere's cipher 
*/

#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[]) {
     
     // Verify number of args is 2
     if (argc != 2) {
         printf("Usage: ./vigenere <keyword>. Exiting.\n");
         return 1;
     }
     
     // keyIndex variable used to cycle over key if input string len > keyLen
     int keyIndex = -1;
     string key = argv[1];
     int len = strlen(key);
     
     if (argc == 2) {
         for (int i = 0; i < len; i++) {
             
             // Check if key character isnt alphabetical
             if (!(isalpha(key[i]))) {
                 printf("Keyword must contain alphabetical characters only. Exiting.\n");
                 return 1;
             }
             
             // convert all key characters to lowercase
             else {
                 key[i] = tolower(key[i]);
             }
         }
     }
    
     printf("plaintext: ");
     string s = get_string();
     printf("ciphertext: ");

     /* Core logic to encrypt input string
        If input char is alphabetical, encrypt differently if
        uppercase or lowercase and increment keyIndex, otherwise
        move to next char of input string, but dont increment index */
     for (int i = 0, textLen = strlen(s); i < textLen; i++) {
         if (isalpha(s[i])) {
             keyIndex++;
             if (isupper(s[i])) {
                 printf("%c", ((s[i] - 'A') + (key[keyIndex % len] - 'a')) % 26 + 'A');
             }
             
             else if (islower(s[i])) {
                 printf("%c", ((s[i] - 'a') + (key[keyIndex % len] - 'a')) % 26 + 'a');
             }
         }
         
         else if (!(isalpha(s[i]))) {
             printf("%c", s[i]);
             continue;
         }
     }
     
     printf("\n");
     return 0;
     
}