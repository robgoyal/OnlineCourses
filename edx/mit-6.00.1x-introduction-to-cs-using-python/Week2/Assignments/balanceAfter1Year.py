# Name: balanceAfter1Year.py
# Author: Robin Goyal
# Last-Modified: October 10, 2017
# Purpose: Calculate the remaining balance after one year if only
#          minimum payment is made
# Note: Attempted a recursive definition to test knowledge

def remainingBalanceAfterYear(balance, annualInterestRate, monthlyPaymentRate, month = 0):
    '''
    balance: outstanding initial balance
    annualInterestRate: annualInterest rate for unpaid balance
    monthlyPaymentRate: minimum monthly payment of balance

    output: outstanding balance after one year
    '''

    # Print remaining balance after end of year
    if month == 12:
        print("Remaining balance: {}".format(round(balance, 2)))

    else:

        # Calculate monthly payment and interest accrued in month
        monthlyInterestRate = annualInterestRate / 12
        minimumMonthlyPayment = monthlyPaymentRate * balance
        monthlyUnpaidBalance = balance - minimumMonthlyPayment

        # Calculated updated balance after month
        updatedBalanceMonthly = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance

        # Increment month
        month += 1

        # Call function passing updated balance
        remainingBalanceAfterYear(updatedBalanceMonthly, annualInterestRate, monthlyPaymentRate, month)