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
      fprintf(stderr, "Error: output file could not open. Exiting.\n");
      return 3;
   }

   // Read bmp header information
   BITMAPFILEHEADER* bf = malloc(sizeof(BITMAPFILEHEADER));
   if (bf == NULL)
   {
      // ERROR
   }
   fread(bf, sizeof(BITMAPFILEHEADER), 1, infile);


   // Read bmp file information
   BITMAPINFOHEADER* bi = malloc(sizeof(BITMAPINFOHEADER));
   if (bi == NULL)
   {
      // ERROR
   }

   printf("%c\n", bf->bfType);
   printf("%i\n", bf->bfSize);
   //BITMAPINFOHEADER* bi;



   // Close file pointers
   fclose(infile);
   fclose(outfile);

   return 0;
}