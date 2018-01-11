# Name: isTriangular.py
# Author: Robin Goyal
# Last-Modified: January 6, 2018
# Purpose: Check if a value k is a triangular number

import math


def is_triangular(k):
    '''
    int -> bool

    Return a boolean indicating if k is a
    triangular number. A triangular number is a number
    where the sum of first few natural numbers sum to k

    Examples:
    is_triangular(10) -> True
        1 + 2 + 3 + 4 = 10
    is_triangular(15) -> True
        1 + 2 + 3 + 4 + 5 = 15
    is_triangular(17) -> False
        1 + 2 + 3 + 4 + 5 != 17
        1 + 2 + 3 + 4 + 5 + 6 != 17
    '''

    # Quadratic equation to solve for n natural numbers is:
    # x = ( -3/2 +- sqrt((3/2) ** 2 - 2(-k + 1)) ) / (2 * 1/2)
    # Check if x is an integer which means k is a triangular number
    x = -1.5 + math.sqrt((3 / 2) ** 2 - 2 * (-k + 1)) + 1
    return x.is_integer()


print(is_triangular(6))
print(is_triangular(10))
print(is_triangular(11))
print(is_triangular(1))
