#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Request height from user [1, 8]
    int height;
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);

    for (int row = 1; row <= height; row++)
    {
        // Print (height - row) spaces)
        for (int spaces = 0; spaces < (height - row); spaces++)
        {
            printf(" ");
        }
        // Print (row) hashes
        for (int hashes = 0; hashes < row; hashes++)
        {
            printf("#");
        }
        // Print newline character for next row
        printf("\n");
    }
}
