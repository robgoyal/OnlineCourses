/* Robin Goyal */
/* Determine whether a credit card is valid using Luhn's algorithm */

#include <stdio.h>
#include <cs50.h>
#include <math.h>
#include <string.h>

int main(void) {
    
    // Store user input of credit card number
    
    long long cardNum;
    
    // Obtain a positive value user input
    do {
        printf("Number: ");
        cardNum = get_long_long();
    } 
    while(cardNum < 0);
    
    int nDigits = floor(log10(labs(cardNum))) + 1;
    int cardDigits[nDigits];
    
    // Store cardNum digits in array
    for (int i = 0; i < nDigits; i++) {
        cardDigits[i] = cardNum % 10;
        cardNum = cardNum / 10;
    }
    
    int tmpSum = 0;
    int tmpVal;
    int tmpLength;
    
    // checksum algorithm
    for (int i = 1; i <= nDigits-1; i = i + 2) {
        
        tmpVal = cardDigits[i] * 2;
        tmpLength = floor(log10(abs(tmpVal))) + 1;
        
        for (int j = 0; j < tmpLength; j++){
            tmpSum += tmpVal % 10;
            tmpVal = tmpVal / 10;
        }
    }
    
    for (int i = 0; i < nDigits; i = i + 2) {
        tmpSum += cardDigits[i];
    }
    
    
    // Determines the validity of the card and card type
    if (tmpSum % 10 == 0) {
        
        if ((cardDigits[nDigits-1]) == 4) {
            printf("VISA\n");
        }
        
        else if( (cardDigits[nDigits-1] == 5) && (cardDigits[nDigits-2] == 1 || cardDigits[nDigits-2] == 2 || cardDigits[nDigits-2] == 3 || 
        cardDigits[nDigits-2] == 4 || cardDigits[nDigits-2] == 5) ) {
            printf("MASTERCARD\n"); 
        }
        
        else if (cardDigits[nDigits-1] == 3 && (cardDigits[nDigits-2] == 4 || cardDigits[nDigits-2] == 7)) {
            printf("AMEX\n");
        }
    }
    
    else {
        printf("INVALID\n");
    }
    
    
    return 0;
}