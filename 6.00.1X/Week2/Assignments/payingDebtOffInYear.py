# Name: payingDebtOffInYear.py
# Author: Robin Goyal
# Last-Modified: October 26, 2017
# Purpose: Find a fixed monthly payment which will pay off all debt in one year

def payingDebtOffInYear(balance, annualInterestRate):
    '''
    balance: outstanding initial balance
    annualInterestRate: yearly interest rate
    
    output: fixed monthly payment required to pay off balance
            as a multiple of 10
    '''

    # Fixed payment initialization
    fixed = 0
    tempBalance = balance

    # Increment fixed payment until balance is paid off
    while(tempBalance >= 0):

        fixed += 10
        tempBalance = balance

        # Determine tempBalance after 12 monthly payments
        for i in range(12):
            tempBalance = (tempBalance - fixed) + (annualInterestRate/12 * (tempBalance - fixed))

    return fixed