/* Calculate the water usage in a shower to bottles of drinking water */

#include <stdio.h>
#include <cs50.h>

int main(void) 
{
    printf("Minutes: ");
    // Obtain user input on number of minutes spent in shower
    int minutes = get_int();
    
    // prints the number of bottles wasted to console
    printf("Bottles: %i\n", minutes * 12);
}