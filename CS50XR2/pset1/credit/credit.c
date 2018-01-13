/* Name: credit.c
   Author: Robin Goyal
   Last-Modified: January 12, 2018
   Purpose: Determine whether a credit card number is valid
*/

#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void)
{

    // Get credit card number
    long long card_number = get_long_long("Number: ");

    // Calculate number of digits in credit card
    int card_len = floor(log10(card_number)) + 1;


    // Declare array of size card_len and convert card digits to array
    int card_digits[card_len];

    for (int i = 0; i < card_len; i++)
    {
        card_digits[card_len - i - 1] = card_number % 10;
        card_number /= 10;
    }

    // Length of card number is even
    bool card_len_even = card_len % 2 == 0;

    // Calculate the sum specificed by luhn's algorithm
    int luhn_sum = 0;

    // Iterate over the individual digits of the card
    for (int i = 0; i < card_len; i++)
    {
        if ((card_len_even && i % 2 == 0) || (!(card_len_even) && i % 2 == 1))
        {

            // Add individual digits of the temporary number to luhn sum
            int temp = 2 * card_digits[i];

            while (temp > 0)
            {
                luhn_sum += temp % 10;
                temp /= 10;
            }
        }

        else
        {
            luhn_sum += card_digits[i];
        }
    }


    // Check if credit card number is valid and print the type of card
    if (luhn_sum % 10 == 0)
    {
        if (card_digits[0] == 3 && (card_digits[1] == 4 || card_digits[1] == 7))
        {
            printf("AMEX\n");
        }

        else if (card_digits[0] == 4)
        {
            printf("VISA\n");
        }

        else
        {
            printf("MASTERCARD\n");
        }
    }

    else
    {
        printf("INVALID\n");
    }
}
