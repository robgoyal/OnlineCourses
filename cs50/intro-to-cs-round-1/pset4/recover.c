#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[]) {
    
    // Check if number of arguments is 2
    if (argc != 2) {
        fprintf(stderr, "Usage: ./recover infile\n");
        return 1;
    }
    
    // Store file in infile
    char* infile = argv[1];
    
    // Open infile argument
    FILE* memory_card = fopen(infile, "r");
    
    // Check if file opened successfully
    if (memory_card == NULL) {
        fprintf(stderr, "Could not open %s.\n", infile);
        return 2;
    }
    
    // Allocate memory to store 512 bytes
    unsigned char* block = malloc(512);
    
    // Iterator variable to increment jpg filenumber
    int file_num = 0;
    
    // Create an outfile with default NULL
    FILE* outfile = NULL;
    
    // Loop through memory until block of memory is less than 512 bytes indicating EOF
    while (fread(block, 1, 512, memory_card) == 512) {
        
        // Check if first 4 bytes is JPEG header
        if (block[0] == 0xff && block[1] == 0xd8 && block[2] == 0xff && (block[3] & 0xf0) == 0xe0) {
            
            // Close previous outfile
            if (outfile != NULL) {
                fclose(outfile);
            }
            
            // Create a new outfile
            char filename[7];
            sprintf(filename, "%03i.jpg", file_num);
            
            // Open outfile with name filename
            outfile = fopen(filename, "w");
            
            // Check if outfile opened succesfully
            if (outfile == NULL) {
                fprintf(stderr, "Could not open %s.\n", filename);
                return 2;
            }
            
            // Increment file number for next filename
            file_num++;
        }
        
        // If JPEG header was found before, write the block to outfile
        if (outfile != NULL) {
            fwrite(block, 1, 512, outfile);
        }
        
    }
    
    // Free allocated memory
    free(block);
    
    // Close final outfile and infile
    fclose(outfile);
    fclose(memory_card);
    
    return 0;
}