/* Name: resize.c
   Author: Robin Goyal
   Last-Modified: February 15, 2018
   Purpose: Implement a program which resizes BMP's
*/

#include <stdio.h>
#include <stdlib.h>
#include "bmp.h"

int main(int argc, char** argv)
{
    // Check if 3 command line arguments are provided
    if (argc != 4)
    {
        fprintf(stderr, "Usage: ./resize n infile outfile\n");
        return 1;
    }

    int factor = atoi(*(argv + 1));

    // Check that the factor is between 1 and 100
    if (factor < 1 || factor > 100)
    {
        fprintf(stderr, "Error: the factor must be between 1 and 100. Exiting.\n");
        return 1;
    }

    // Open input file
    FILE* infile = fopen(*(argv + 2), "r");
    if (infile == NULL)
    {
        fprintf(stderr, "Error: input file could not open. Exiting.\n");
        return 1;
    }

    // Open output file
    FILE* outfile = fopen(*(argv + 3), "w");
    if (outfile == NULL)
    {
        fprintf(stderr, "Error: output file could not open. Exiting.\n");
        return 1;
    }

    // Allocate memory for BMP header structs
    BITMAPFILEHEADER* bf = malloc(sizeof(BITMAPFILEHEADER));
    BITMAPINFOHEADER* bi = malloc(sizeof(BITMAPINFOHEADER));

    // Read infile's BMP info header and file header
    fread(bf, sizeof(BITMAPFILEHEADER), 1, infile);
    fread(bi, sizeof(BITMAPINFOHEADER), 1, infile);

    // Check if memory allocation occurred
    if (bf == NULL || bi == NULL)
    {
        fclose(infile);
        fclose(outfile);
        fprintf(stderr, "Error: memory allocation failed. Exiting.\n");
        return 1;
    }

    // Check if input is 24-bit Uncompressed BMP 4.0
    if (bf->bfType != 0x4D42 || bi->biBitCount != 24 || bi->biCompression != 0 || bi->biSize != 40)
    {
        fclose(infile);
        fclose(outfile);
        fprintf(stderr, "Error: invalid input file format. Exiting.\n");
        return 1;
    }

    // Padding from input file
    int inputpadding = (4 - (bi->biWidth * 3) % 4) % 4;

    // Scaled padding for output file
    int outputpadding = (4 - (bi->biWidth * factor * 3) % 4) % 4;

    // Update outfile header information
    bi->biWidth = bi->biWidth * factor;
    bi->biHeight = bi->biHeight * factor;

    bi->biSizeImage = (bi->biWidth * 3 + outputpadding) * abs(bi->biHeight);
    bf->bfSize = sizeof(*bf) + sizeof(*bi) + bi->biSizeImage;

    // Write updated file headers to outfile
    fwrite(bf, sizeof(*bf), 1, outfile);
    fwrite(bi, sizeof(*bi), 1, outfile);

    // Initialize scaled scanline for output file
    RGBTRIPLE** newscanline = (RGBTRIPLE**) malloc(sizeof(RGBTRIPLE*) * bi->biWidth);

    // Iterate through scanlines of input file
    for (int row = 0, oldheight = abs(bi->biHeight) / factor; row < oldheight; row++)
    {

        // Iterate through pixels in scanline from input file
        for (int col = 0, oldwidth = bi->biWidth / factor; col < oldwidth; col++)
        {
            // Read in pixel
            RGBTRIPLE* pixel = (RGBTRIPLE*) malloc(sizeof(RGBTRIPLE));
            fread(pixel, sizeof(RGBTRIPLE), 1, infile);

            // Copy pixel in new scanline factor times
            for (int i = 0; i < factor; i++)
            {
                *(newscanline + (factor*col + i)) = pixel;
            }
        }

        // Skip over padding in input file
        fseek(infile, inputpadding, SEEK_CUR);

        // Write newscanline factor times to output file
        for (int repeat = 0; repeat < factor; repeat++)
        {
            // Write each pixel in new scanline
            for (int i = 0; i < bi->biWidth; i++)
            {
                fwrite(*(newscanline + i), sizeof(RGBTRIPLE), 1, outfile);
            }

            // Write padding to output file
            for (int padding = 0; padding < outputpadding; padding++)
            {
                fputc(0x00, outfile);
            }
        }

        // Free allocated memory for pixels
        for (int i = 0, oldwidth = bi->biWidth / factor; i < oldwidth; i++)
        {
            free(newscanline[factor*i]);
        }
    }

    // Free allocated memory for new scanline
    free(newscanline);

    // Free memory allocated to structures
    free(bf);
    free(bi);

    // Close file pointers
    fclose(infile);
    fclose(outfile);
    return 0;
}