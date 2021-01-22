#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>


int main(int argc, string argv[])
{
    // Validate that there is a single command line argument
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

    string key = argv[1];
    int length = strlen(key);

    // Validate that there are 26 characters in the key
    if (length != 26)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }

    // Validate that there are only alphabetic characters
    for (int i = 0; i < length; i++)
    {
        if (!(isalpha(key[i])))
        {
            printf("Key must contain alphabetic characters only.\n");
            return 1;
        }
    }

    // Validate that the key contains each letter of alphabet exactly once
    int alphabet_mask[26] = {0};
    for (int i = 0; i < length; i++)
    {
        alphabet_mask[tolower(key[i]) - 97]++;
    }
    for (int i = 0; i < 26; i++)
    {
        if (alphabet_mask[i] == 0)
        {
            printf("Key must contain all letters of alphabet exactly once.\n");
            return 1;
        }
    }

    // Request plaintext input from user
    string plaintext = get_string("plaintext: ");

    printf("ciphertext: ");

    for (int i = 0, n = strlen(plaintext); i < n; i++)
    {
        char p = plaintext[i];

        // Substitution of upper and lower chars are based on ASCII values
        if (isupper(p))
        {
            printf("%c", toupper(key[(p - 65)]));
        }
        else if (islower(p))
        {
            printf("%c", tolower(key[(p - 97)]));
        }
        else
        {
            // No substitution if not alphabetic
            printf("%c", p);
        }
    }

    printf("\n");
    return 0;
}
