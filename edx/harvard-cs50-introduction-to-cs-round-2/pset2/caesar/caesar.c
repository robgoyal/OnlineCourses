#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


bool is_valid_arg(int argc, string argv[]);


int main(int argc, string argv[])
{
    // Validate for a single positive integer command line argument
    if (!(is_valid_arg(argc, argv)))
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    // Convert string argument to integer
    int key = atoi(argv[1]);

    // Request plaintext input from user
    string plaintext = get_string("plaintext: ");

    printf("ciphertext: ");

    for (int i = 0, n = strlen(plaintext); i < n; i++)
    {
        char p = plaintext[i];

        // Rotate by upper
        if (isupper(p))
        {
            printf("%c", ((p - 65) + key) % 26 + 65);
        }
        else if (islower(p))
        {
            printf("%c", ((p - 97) + key) % 26 + 97);
        }
        else
        {
            // No rotation if not alphabetic
            printf("%c", p);
        }
    }

    printf("\n");
    return 0;
}


/* Return true if valid argument, false otherwise
   Arguments are not valid if:
    - more than 1 argument is provided
    - argument is not of type number
    - not a positive integer */
bool is_valid_arg(int argc, string argv[])
{
    if (argc != 2)
    {
        return false;
    }

    // If negative number is provided, this returns false
    // since hyphen ( - ) character is not a digit
    string key = argv[1];
    for (int i = 0, n = strlen(key); i < n; i++)
    {
        if (!(isdigit(key[i])))
        {
            return false;
        }
    }

    return true;
}