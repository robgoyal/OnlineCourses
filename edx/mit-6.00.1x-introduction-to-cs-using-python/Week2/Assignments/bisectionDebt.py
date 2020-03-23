# Name: bisectionDebt.py
# Author: Robin Goyal
# Last-Modified: October 26, 2017
# Purpose: Calculate a fixed monthly payment to pay off all debt in
#          one year using bisection search

def bisectionDebt(balance, annualInterestRate):
    '''
    balance: outstanding initial balance
    annualInterestRate: yearly interest rate
    
    output: fixed monthly payment required to pay off balance
            as a multiple of 0.01 (one cent)
    '''

    # Minimum remaining balance (one cent)
    epsilon = 0.01

    # Initial lower and upper bounds
    lowerFixedPayment = balance / 12
    higherFixedPayment = (balance * (1 + annualInterestRate/12) ** 12)/12

    # Calculate initial fixed value
    fixed = (higherFixedPayment + lowerFixedPayment) / 2

    tempBalance = balance

    # Falls within one cent of either range
    while(not(-epsilon < tempBalane < epsilon)):

        # Update temporary balance
        tempBalance = balance

        # Calculate balance remaining after 12 fixed payments
        for i in range(12):
            tempBalance = (tempBalance - fixed) + (annualInterestRate/12 * (tempBalance - fixed))

        # Set fixed payment to middle of lower range if balance remaining is low
        if (tempBalance < -0.01):
            higherFixedPayment = fixed
            fixed = (lowerFixedPayment + fixed)/2

        # Set fixed payment to middle of higher range if balance remaining is high
        elif (tempBalance > 0.01):
            lowerFixedPayment = fixed
            fixed = (fixed + higherFixedPayment)/2

    # Round to two decimal places
    return "{0:.2f}".format(fixed)

bisectionDebt(320000, 0.2)