"""
Module = python file that we can import into your current python file
"""
import random
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

feet_in_mile = 5280
meters_in_kilometer = 1000
beatles = ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Star"]

def get_file_ext(filename):
    return filename[filename.index(".") + 1:]

def roll_dice(num):
    return random.randint(1,num)