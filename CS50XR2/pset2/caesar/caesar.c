/* Name: caesar.c
   Author: Robin Goyal
   Last-Modified: January 20, 2018
   Purpose: A program which encrypts messages using Caesar's cipher
*/

#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>


int main(int argc, string argv[])
{
    // Check that the number of arguments is 2 (including name of program)
    if (argc != 2)
    {
        printf("Usage: ./caesar k\n");
        return 1;
    }

    // Convert string to integer
    int k = atoi(argv[1]);

    // Get plaintext from user
    string plaintext = get_string("plaintext: ");

    // Prepare to print out the ciphertext
    printf("ciphertext: ");

    for (int i = 0, n = strlen(plaintext); i < n; i++)
    {
        if (isalpha(plaintext[i]))
        {
            if (islower(plaintext[i]))
            {
                // Print lowercase char rotated by k accounting for wrapping
                printf("%c", (plaintext[i] - 'a' + k) % 26 + 'a');
            }

            else
            {
                // Print uppercase char rotated by k accounting for wrapping
                printf("%c", (plaintext[i] - 'A' + k) % 26 + 'A');
            }
        }

        else
        {

            // Print non-alphabetical char with no modifications
            printf("%c", plaintext[i]);
        }
    }

    printf("\n");

    return 0;
}