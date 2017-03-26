/**
 * Enlarges a BMP file by argument n
 */
       
#include <stdio.h>
#include <stdlib.h>

#include "bmp.h"

int main(int argc, char *argv[])
{
    // ensure proper usage
    if (argc != 4)
    {
        fprintf(stderr, "Usage: ./resize size infile outfile\n");
        return 1;
    }
    
    int scale = atoi(argv[1]);
    
    // Check if 2nd argument is less than 100
    if (scale > 100)
    {
        fprintf(stderr, "Size argument must be less than 100\n");
        return 1;
    }
    
    // remember filenames
    char *infile = argv[2];
    char *outfile = argv[3];

    // open input file 
    FILE *inptr = fopen(infile, "r");
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", infile);
        return 1;
    }

    // open output file
    FILE *outptr = fopen(outfile, "w");
    if (outptr == NULL)
    {
        fclose(inptr);
        fprintf(stderr, "Could not create %s.\n", outfile);
        return 1;
    }

    // read infile's BITMAPFILEHEADER
    BITMAPFILEHEADER bf;
    fread(&bf, sizeof(BITMAPFILEHEADER), 1, inptr);

    // read infile's BITMAPINFOHEADER
    BITMAPINFOHEADER bi;
    fread(&bi, sizeof(BITMAPINFOHEADER), 1, inptr);

    // ensure infile is (likely) a 24-bit uncompressed BMP 4.0
    if (bf.bfType != 0x4d42 || bf.bfOffBits != 54 || bi.biSize != 40 || 
        bi.biBitCount != 24 || bi.biCompression != 0)
    {
        fclose(outptr);
        fclose(inptr);
        fprintf(stderr, "Unsupported file format.\n");
        return 4;
    }
    

    // Determine old padding
    int old_padding = (4 - (bi.biWidth * sizeof(RGBTRIPLE)) % 4) % 4; 
    
    // Updated file header info based off scale
    bi.biWidth = bi.biWidth * scale;
    bi.biHeight = bi.biHeight * scale;
    
    // Determine scaled padding
    int scaled_padding = (4 - (bi.biWidth * sizeof(RGBTRIPLE)) % 4) % 4;
    
    bi.biSizeImage = ((sizeof(RGBTRIPLE) * bi.biWidth) + scaled_padding) * (abs(bi.biHeight));
    bf.bfSize = bi.biSizeImage + sizeof(BITMAPFILEHEADER) + sizeof(BITMAPINFOHEADER);
    
    // write outfile's BITMAPFILEHEADER
    fwrite(&bf, sizeof(BITMAPFILEHEADER), 1, outptr);

    // write outfile's BITMAPINFOHEADER
    fwrite(&bi, sizeof(BITMAPINFOHEADER), 1, outptr);

    // Allocate memory for new bmp width
    char* scaled_row = malloc(sizeof(RGBTRIPLE) * bi.biWidth);
    
    // iterate over infile's scanlines
    // biHeight divided by scale so only iterating through number of infile scanlines
    for (int i = 0, biHeight = abs(bi.biHeight)/scale; i < biHeight; i++)
    {
        // Pointer to keep track of allocated memory
        int pointer = 0; 
        
        // iterate over pixels in scanline
        // biWidth divided by scale to only iterate through number of infile pixels
        for (int j = 0; j < bi.biWidth/scale; j++)
        {
            // temporary storage
            RGBTRIPLE triple;

            // read RGB triple from infile
            fread(&triple, sizeof(RGBTRIPLE), 1, inptr);
            
            // Storing triple in allocated memory
            for (int k = 0; k < scale; k++) 
            {
                scaled_row[pointer] = triple.rgbtBlue;
                scaled_row[pointer+1] = triple.rgbtGreen;
                scaled_row[pointer+2] = triple.rgbtRed;
                pointer = pointer + 3;
            }
            // write RGB triple to outfile
            //fwrite(&triple, sizeof(RGBTRIPLE), 1, outptr);
        }
        
        // Iterate through scale to vertically enlarge pixels
        for (int j = 0; j < scale; j++) {
            
            // Write stored row memory to outfile
            fwrite(scaled_row, sizeof(RGBTRIPLE) * bi.biWidth, 1, outptr);
            
            // Place padding in outfile based off scaled_padding
            for (int k = 0; k < scaled_padding; k++) {
                fputc(0x00, outptr);
            }
        }

        // skip over padding, if any in infile
        fseek(inptr, old_padding, SEEK_CUR);
    }

    // Free allocated memory
    free(scaled_row);
    
    // close infile
    fclose(inptr);

    // close outfile
    fclose(outptr);

    // success
    return 0;
}
