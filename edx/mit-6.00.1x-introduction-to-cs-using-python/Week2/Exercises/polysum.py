# Name: polysum.py
# Author: Robin Goyal
# Last-Modified: October 10, 2017
# Purpose: Calculate the sum of the area + perimeter squared

import math

def polysum(n, s):

    # Calculate area of polygon
    area = (0.25 * n * math.pow(s, 2)) / math.tan(math.pi/n)

    # Calculate the perimeter of polygon
    perimeter = n * s

    # Return sum rounded to 4 digits
    return round(area + math.pow(perimeter, 2), 4)