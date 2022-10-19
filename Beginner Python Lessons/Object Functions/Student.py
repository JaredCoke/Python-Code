"""
Class Functions: A function that we can use inside of a class to modify the objects of that class
"""
class Student:
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            #print(" is on honor roll.") #To Do: Add object name
            return True
        else:
            #print(" is not on honor roll.") #To Do: Add object name
            return False