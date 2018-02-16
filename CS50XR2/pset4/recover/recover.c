/* Name: recover.c
   Author: Robin Goyal
   Last-Modified: February 16, 2018
   Purpose: Recover JPEG images from a memory card
*/

#include <stdio.h>
#include <stdbool.h>

bool is_jpeg(unsigned char block[512]);

int main(int argc, char** argv)
{
    // Verify two arguments were passed
    if (argc != 2)
    {
        fprintf(stderr, "Usage: ./recover image\n");
        return 1;
    }

    // Open file for reading
    FILE* card = fopen(*(argv + 1), "r");
    if (card == NULL)
    {
        fprintf(stderr, "Error: file could not be opened. Exiting.\n");
        return 2;
    }

    // Initialize file information
    char filename[8];
    int filenumber = 0;

    unsigned char block[512];

    while (true)
    {
        fread(block, sizeof(block), 1, card);

        if (is_jpeg(block))
        {
            // Open file for writing
            sprintf(filename, "%03d.jpg", filenumber);
            FILE* jpeg = fopen(filename, "w");
            if (jpeg == NULL)
            {
                fprintf(stderr, "Error: jpeg file could not be opened for writing. Exiting.\n");
                return 2;
            }

            fwrite(block, sizeof(block), 1, jpeg);
            while (1)
            {
                fread(block, sizeof(block), 1, card);

                if (is_jpeg(block))
                {
                    fclose(jpeg);
                    break;
                }

                fwrite(block, sizeof(block), 1, jpeg);
            }

            break;
        }
    }

    // fread(block, sizeof(block), 1, card);

    // for (int i = 0; i < 1024; i++)
    // {
    //     printf("%i ", block[i]);
    // }

    printf("\n");

    sprintf(filename, "%03d.jpg", filenumber);
    printf("%s\n", filename);
    fclose(card);
    return 0;
}


// Check if first set of bytes are of type JPEG
bool is_jpeg(unsigned char block[512])
{
    return (block[0] == 255 && block[1] == 216 && block[2] == 255 && ((block[3] & 224) == 224));
}