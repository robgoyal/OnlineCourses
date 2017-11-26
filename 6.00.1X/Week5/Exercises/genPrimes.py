# Name: genPrimes.py
# Author: Robin Goyal
# Last-Modified: November 25, 2017
# Purpose: Create a generator which returns prime numbers


def isPrime(x):
    '''
    x: int
    return: boolean

    True if x is prime, else False
    '''

    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def primes():

    start = 2
    while True:

        if isPrime(start):
            yield start

        start += 1
