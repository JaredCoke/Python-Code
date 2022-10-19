# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
try:
    number = int(input("Enter your favorite number, por favor: "))
    print(number)
    print(20/number)

except ValueError as err:
    print('Ha! You triggered my trap card!')
    print(err)
except TypeError as err:
    print('Ha! You triggered my trap card!')
    print(err)
except ZeroDivisionError as err:
    print('Ha! You triggered my trap card!')
    print(err)
