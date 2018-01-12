/* Name: mario.c
   Author: Robin Goyal
   Last-Modified: January 12, 2018
   Purpose: Print the double pyramids from Mario with a specified height
*/

#include <stdio.h>
#include <cs50.h>


int main(void)
{

   // Get int between 1 and 23
   int height;

   do
   {
      height = get_int("Height: ");
   } while(height < 0 || height > 23);


   for (int row = 1; row <= height; row++)
   {

      // Print spaces for left half
      for (int i = 0; i < height - row; i++)
      {
         printf(" ");
      }

      // Print blocks for left half
      for (int i = 0; i < row; i++)
      {
         printf("#");
      }

      // Print two spaces between pyramids
      printf("  ");

      // Print blocks for right half
      for (int i = 0; i < row; i++)
      {
         printf("#");
      }

      // Terminate line
      printf("\n");
   }
}