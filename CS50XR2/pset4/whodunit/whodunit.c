/* Name: whodunit.c
   Author: Robin Goyal
   Last-Modified: February 13, 2018
   Purpose: Determine who committed the crime by the
            clue in the picture.
*/

#include <stdio.h>
#include <stdlib.h>
#include "bmp.h"

int main(int argc, char** argv)
{
   // Check if two command line arguments are included
   if (argc != 3)
   {
      fprintf(stderr, "Usage: ./whodunit infile outfile\n");
      return 1;
   }

   FILE* infile = fopen(*(argv + 1), "r");

   // Check if input file opens
   if (infile == NULL)
   {
      fprintf(stderr, "Error: input file could not open. Exiting.\n");
      return 2;
   }

   FILE* outfile = fopen(*(argv + 2), "w");

   // Check if output file opens
   if (outfile == NULL)
   {
      fclose(infile);
      fprintf(stderr, "Error: output file could not open. Exiting.\n");
      return 3;
   }

   // Initialize memory for pointers for BMP headers
   BITMAPFILEHEADER* bf = malloc(sizeof(BITMAPFILEHEADER));
   BITMAPINFOHEADER* bi = malloc(sizeof(BITMAPINFOHEADER));

   // Check if memory allocation was successful
   if (bf == NULL || bi == NULL)
   {
      fclose(infile);
      fclose(outfile);
      fprintf(stderr, "Error: memory allocation failed. Exiting.\n");
      return 5;
   }

   // Read file header information
   fread(bf, sizeof(BITMAPFILEHEADER), 1, infile);
   fread(bi, sizeof(BITMAPINFOHEADER), 1, infile);

   // Check if input BMP file is 24-bit uncompressed BMP 4.0
   if ((bi->biBitCount != 24) || (bi->biCompression != 0) || (bi->biSize != 40) || (bf->bfType != 0x4d42))
   {
      fclose(infile);
      fclose(outfile);
      fprintf(stderr, "Error: infile is not a valid BMP file format. Exiting.\n");
      return 4;
   }

   // Write header information to new file
   fwrite(bf, sizeof(BITMAPFILEHEADER), 1, outfile);
   fwrite(bi, sizeof(BITMAPINFOHEADER), 1, outfile);

   // Calculate number of bytes required for padding in input file
   int padding = (4 - (bi->biWidth * sizeof(RGBTRIPLE)) % 4) % 4;

   // Iterate over the number of scanlines in BMP
   for (int row = 0, height = abs(bi->biHeight); row < height; row++)
   {

      // Iterate over each pixel in scanline
      for (int col = 0, width = bi->biWidth; col < width; col++)
      {

         // Read in rgb pixel
         RGBTRIPLE* pixel = malloc(sizeof(RGBTRIPLE));
         fread(pixel, sizeof(RGBTRIPLE), 1, infile);

         // Remove color for pixel if it contains full red
         if (pixel->rgbtRed == 0xFF)
         {
            pixel->rgbtRed = 0;
            pixel->rgbtBlue = 0;
            pixel->rgbtGreen = 0;
         }

         // Write updated pixel to outfile
         fwrite(pixel, sizeof(RGBTRIPLE), 1, outfile);
         free(pixel);
      }

      // Skip over padding in infile
      fseek(infile, sizeof(char) * padding, SEEK_CUR);

      // Write padding number of 0's to outfile
      for (int i = 0; i < padding; i++)
      {
         fputc(0, outfile);
      }

   }

   // Free allocated memory for headers
   free(bf);
   free(bi);

   // Close file pointers
   fclose(infile);
   fclose(outfile);

   return 0;
}
