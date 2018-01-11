# Name: Container.py
# Author: Robin Goyal and MIT 6.00.1X
# Last-Modified: January 10, 2018
# Purpose: Create a class ASet which inherits Container
#          and creates methods remove and is_in


class Container(object):
    """ Holds hashable objects. Objects may occur 0 or more times """

    def __init__(self):
        """ Creates a new container with no objects in it. I.e., any object
            occurs 0 times in self. """
        self.vals = {}

    def insert(self, e):
        """ assumes e is hashable
            Increases the number times e occurs in self by 1. """
        try:
            self.vals[e] += 1
        except:
            self.vals[e] = 1

    def __str__(self):
        s = ""
        for i in sorted(self.vals.keys()):
            if self.vals[i] != 0:
                s += str(i) + ":" + str(self.vals[i]) + "\n"
        return s


class ASet(Container):
    def remove(self, e):
        """
        assumes e is hashable
        removes e from self
        """

        del self.vals[e]

    def is_in(self, e):
        """
        assumes e is hashable
        returns True if e has been inserted in self and
        not subsequently removed, and False otherwise.
        """

        return e in self.vals
