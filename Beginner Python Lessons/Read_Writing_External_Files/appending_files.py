# This file imports my reading user class
from reading_files import Reading_Files

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
try:
    data_from_text_file = open("readable_text.txt", "a") #open the file for writing

    answer = input("What is your name: ")
    data_from_text_file.write(answer + "\nIm sinking!")

    #data_from_text_file = open("readable_text.txt", "r")  # open the file for reading
    # create an object
    # create
    filename1 = Reading_Files("readable_text.txt")
    print(filename1.filename)

    data_from_text_file = open(filename1.filename, "r")  # open the file for writing
    print(data_from_text_file.read()) #prints all data stored in this file
    data_from_text_file.close #close the file

except ValueError as err:
    print('Ha! You triggered my trap card!')
    print(err)
except TypeError as err:
    print('Ha! You triggered my trap card!')
    print(err)
except ZeroDivisionError as err:
    print('Ha! You triggered my trap card!')
    print(err)
except IndexError as err:
    print('Ha! You triggered my trap card!')
    print(err)