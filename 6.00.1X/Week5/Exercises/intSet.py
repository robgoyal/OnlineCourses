# Name: intSet.py
# Author: Robin Goyal and MIT Staff
# Last-Modified: November 21, 2017
# Purpose: Implement an intersect and length function for intSet class


class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if e not in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    def __len__(self):
        '''
        Calculate length of set
        '''

        return len(self.vals)

    def intersect(self, other):
        '''
        Create new intSet with same elements from each set
        '''

        common = intSet()
        for elem in self.vals:
            if other.member(elem):
                common.insert(elem)

        return common
