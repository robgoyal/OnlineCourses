# Name: Person.py
# Author: Robin Goyal and MIT 6.00.1X
# Last-Modified: January 10, 2018
# Purpose: Modify the ArrogantProfessor class to say specific sentences


class Person(object):
    def __init__(self, name):
        self.name = name

    def say(self, stuff):
        return self.name + ' says: ' + stuff

    def __str__(self):
        return self.name


class Lecturer(Person):
    def lecture(self, stuff):
        return 'I believe that ' + Person.say(self, stuff)


class Professor(Lecturer):
    def say(self, stuff):
        return self.name + ' says: ' + self.lecture(stuff)


class ArrogantProfessor(Professor):
    def say(self, stuff):
        return self.name + " says: " + self.lecture(stuff)

    def lecture(self, stuff):
        return "It is obvious that " + self.name + " says: " + stuff


e = Person('eric')
le = Lecturer('eric')
pe = Professor('eric')
ae = ArrogantProfessor('eric')
print(ae.say('the sky is blue'))
