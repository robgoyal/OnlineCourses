#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <cs50.h>


/* Calculate the US grade reading level for a passage
   of text using the Coleman-Liau index */
int main(int argc, string argv[])
{
    string text = get_string("Text: ");

    int letters = 0, spaces = 0, sentences = 0, words;

    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (isalpha(text[i]))
        {
            // Account for uppercase and lowercase letters
            letters++;
        }
        else if (text[i] == ' ')
        {
            spaces++;
        }
        else if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            // A period, exclamation or question mark indicates the end of a sentence
            sentences++;
        }
    }

    // Two words surround a space which is why we increment by 1
    words = spaces + 1;

    // The index requires the number of letters and sentences per 100 words
    float multiplier = (float) 100 / (float) words;

    // Calculate the index using Coleman-Liau formula
    int index = round(0.0588 * (letters * multiplier) - 0.296 * (sentences * multiplier) - 15.8);

    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }

}