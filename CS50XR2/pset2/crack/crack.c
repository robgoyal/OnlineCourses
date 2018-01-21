/* Name: crack.c
   Author: Robin Goyal
   Last-Modified: January 21, 2018
   Purpose: Implement a program which cracks passwords encrypted
            by C's DES based crypt function
*/

#define _XOPEN_SOURCE
#include <unistd.h>
#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

const string LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

int main(int argc, string argv[])
{
    // Check if 2 arguments were passed
    if (argc != 2)
    {
        printf("Usage: ./crack hash\n");
        return 1;
    }

    string hash = argv[1];

    // Declare salt array of size 3 to account for null terminating char
    char salt[3];

    // First two bytes (characters) of hash is the salt
    strncpy(salt, hash, 2);

    // Store length of all possible alphabetical characters
    int len = 52;

    // Possible length of password ranges from 1 to 5 characters
    for (int i = 1; i <= 5; i++)
    {
        char guess[i];

        // 52**i possible values for guess of length i
        for (int j = 0; j < (int) pow(len, i); j++)
        {
            int temp = j;

            for (int k = 0; k < i; k++)
            {

                if (k == (i - 1))
                {
                    // Last character of guess is remaining value in temp
                    guess[k] = LETTERS[temp % len];
                }

                else
                {
                    // Place value logic to determine letter for position k
                    int placevalue = (int) pow(len, i - k - 1);

                    guess[k] = LETTERS[temp / placevalue];
                    temp = temp % (int) placevalue;
                }
            }

            // Check if hashed guess is equal to original hash
            if (strcmp(crypt(guess, salt), hash) == 0)
            {
                printf("%s\n", guess);
                return 0;
            }
        }
    }
}
