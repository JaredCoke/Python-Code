# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import main


def print_number(answer):
    # Use a breakpoint in the code line below to debug your script.
    try:
        print(answer)  # Press Ctrl+F8 to toggle the breakpoint.
    except:
        print('Ha! You triggered my trap card!')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    answer = int(input("Enter your favorite number, por favor: "))
    print_number('Hola, your favorite number is ' + answer)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
