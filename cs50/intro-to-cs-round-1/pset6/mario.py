# Name: Mario.py
# Author: Robin Goyal
# Last-Modified: May 24, 2017
# Purpose: Print double pyramids from Mario with height as input


import cs50
import sys

def main():
    
    # Get height input 
    height = getHeight()
    
    # Draw pyramid
    for i in range(1, height + 1):
        forwardPyramid(height, i)
        reversePyramid(height, i)

def forwardPyramid(height, count):
    print(" " * (height - count), end = "")
    print("#" * count, end = "")
    print(" ", end = "")
    
def reversePyramid(height, count):
    print(" ", end = "")
    print("#" * count, end = "")
    print(" " * (height - count))

# Height requirements should be between 1 and 22
def getHeight():
    while True:
        print("Pyramid Height: ", end = "")
        height = cs50.get_int()
        
        if (height >= 0 and height < 23):
            break
    return height
    
if __name__ == "__main__":
    main()