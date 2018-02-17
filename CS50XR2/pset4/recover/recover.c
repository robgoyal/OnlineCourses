/* Name: recover.c
   Author: Robin Goyal
   Last-Modified: February 17, 2018
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

    // Initialize output file jpeg information
    char filename[8];
    int filenumber = 0;

    // Initialize block to read from input file
    unsigned char block[512];

    // Skip file data until reaching first JPEG
    do
    {
        fread(block, sizeof(block), 1, card);
    }
    while(!(is_jpeg(block)));

    // Loop until reaching EOF
    while (!feof(card))
    {
        // Open file for writing
        sprintf(filename, "%03d.jpg", filenumber);
        FILE* jpeg = fopen(filename, "w");
        if (jpeg == NULL)
        {
            fprintf(stderr, "Error: jpeg file could not be opened for writing. Exiting.\n");
            return 2;
        }

        // Write jpeg data until reaching next jpeg file or reaching EOF
        do
        {
            fwrite(block, sizeof(block), 1, jpeg);
            fread(block, sizeof(block), 1, card);
        }
        while (!feof(card) && !is_jpeg(block));

        // Close output jpeg file
        fclose(jpeg);

        // Increment file number for next jpeg file
        filenumber++;
    }

    // Close memory card
    fclose(card);
    return 0;
}

// Check if first set of bytes are of type JPEG
bool is_jpeg(unsigned char block[512])
{
    return (block[0] == 255 && block[1] == 216 && block[2] == 255 && ((block[3] & 224) == 224));
}
