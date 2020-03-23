# Name: coordinate.py
# Author: Robin Goyal and MIT Staff
# Last-Modified: November 21, 2017
# Purpose: Implement an equal and repr method for the Coordinate class


class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def __eq__(self, other):
        '''
        Check if the coordinates have the same points
        '''

        return (self.getX() == other.getX()) and (self.getY() == other.getY())

    def __repr__(self):
        '''
        Function to represent the Coordinate object
        '''

        return "Coordinate({},{})".format(self.getX(), self.getY())
