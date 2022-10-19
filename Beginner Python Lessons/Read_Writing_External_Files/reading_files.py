"""
Make this a class so you can call this in  the writingg & appending scripts.
"""
class Reading_Files:
    # Press Shift+F10 to execute it or replace it with your code.
    # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
    """
    try:
        data_from_text_file = open("readable_text.txt", "r") #open the file

        print(data_from_text_file.readable() )#check if file is readable

        #print(data_from_text_file.read()) #prints all data stored in this file
        #print(data_from_text_file.readline()) #prints data stored on the first/selected line

        for all_data_in_row in data_from_text_file.readlines(): #this loops through each line of the text file
            print(all_data_in_row) #this stores all lines inside a file into a list

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
    """

    def __init__(self, filename):
        self.filename = filename

    """
    def open_file(filename):
        filename = filename
        #data_from_text_file = open("readable_text.txt", "r") #open the file
        data_from_text_file = open(filename, "r") #open the file
        return filename, data_from_text_file
    """

    def check_if_readable(filename):
        data_from_text_file = open(filename, "r") #open the file
        print(data_from_text_file.readable())  # check if file is readable
        return

    def read_file(filename):
        data_from_text_file = open("readable_text.txt", "r")  # open the file

        # print(data_from_text_file.read()) #prints all data stored in this file
        # print(data_from_text_file.readline()) #prints data stored on the first/selected line

        for all_data_in_row in data_from_text_file.readlines():  # this loops through each line of the text file
            print(all_data_in_row)  # this stores all lines inside a file into a list
        return
