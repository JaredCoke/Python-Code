# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
try:
    # create a new file for writing to
    data_from_text_file = open("writeable_text.txt", "w")

    answer = input("What is your name: ")
    data_from_text_file.write("Welcome "+ answer + "\nTo your demise!")

    data_from_text_file = open("writeable_text.txt", "r")  # open the file for reading
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