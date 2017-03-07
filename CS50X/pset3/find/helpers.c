/**
 * helpers.c
 *
 * Helper functions for Problem Set 3.
 */
 
#include <cs50.h>
#include "helpers.h"

bool binarySearch(int needle, int hayStack[], int first, int last);

/**
 * Returns true if value is in array of n values, else false.
 */
bool search(int value, int values[], int n)
{
    // TODO: implement a searching algorithm
    return binarySearch(value, values, 0, n);
}

/**
 * Recursive function call to test if value is the array of values
 * Returns true if value exists otherwise returns false
 */
bool binarySearch(int needle, int hayStack[], int first, int last) {
    
    // Base case of recursive function to test if len of array 
    // has reached 0 which means needle is not in array
    if (last - first < 0) {
        return false;
    }
    
    else {
        int midpoint = (first + last) / 2;
        
        // Test if needle is in greater half of array and recursively call greater half
        if (needle > hayStack[midpoint]) {
            return binarySearch(needle, hayStack, midpoint + 1, last);
        }
        
        // Test if needle is in lower half of array and recursively call lower half
        else if (needle < hayStack[midpoint]) {
            return binarySearch(needle, hayStack, first, midpoint - 1);
        }
        
        // This case indicates that the needle is at the midpoint
        else {
            return true;
        }
    }
    
    
}


/**
 * Sorts array of n values.
 */
void sort(int values[], int n)
{
    int swaps = -1;
    int tmp;
    
    // Exit while loop if no swaps have been made
    while (swaps != 0) {
        swaps = 0;
        
        for (int i = 0; i < n - 1; i++) {
    
            if (values[i] > values[i+1]) {
                
                // Swapping with temporary variable
                tmp = values[i];
                values[i] = values[i+1];
                values[i+1] = tmp;
                
                // Increment swaps to indicate swap has been made
                swaps++;
            }
            
            else {
                continue;
            }
        }
    }
}
