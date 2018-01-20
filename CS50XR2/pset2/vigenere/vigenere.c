/* Name: vigenere.c
   Author: Robin Goyal
   Last-Modified: January 20, 2018
   Purpose: A program which encrypts messages using Vigenere's cipher
*/

#include <stdio.h>
#include <string.h>
#include <cs50.h>
#include <ctype.h>


int main(int argc, string argv[])
{
    // Check if number of arguments is 2 (accounting for )
    if (argc != 2)
    {
        printf("Usage: ./vigenere k\n");
        return 1;
    }

    string key = argv[1];
    int klen = strlen(key);

    // Check if key contains any non-alphabetic characters
    for (int i = 0; i < klen; i++)
    {
        if (!(isalpha(key[i])))
        {
            printf("Usage: ./vigenere k\n");
            return 1;
        }

        // Convert all characters in key to lowercase
        else
        {
            key[i] = tolower(key[i]);
        }
    }

    // Get plaintext from user
    string plaintext = get_string("plaintext: ");

    // Prepare ciphertext output
    printf("ciphertext: ");

    for (int i = 0, j = 0, n = strlen(plaintext); i < n; i++)
    {
        if (isalpha(plaintext[i]))
        {
            if (islower(plaintext[i]))
            {
                // Print lowercase char rotated by key accounting for wrapping of the
                // key as well as wrapping of the letter
                printf("%c", (plaintext[i] - 'a' + (key[j % klen] - 'a')) % 26 + 'a');
            }

            else
            {

                // Print uppercase char rotated by key accounting for wrapping of the
                // key as well as wrapping of the letter
                printf("%c", (plaintext[i] - 'A' + (key[j % klen] - 'a')) % 26 + 'A');
            }

            // Increment key counter only if rotation of a letter occurs
            j++;
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