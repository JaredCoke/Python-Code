"""
Inheritance = Where you can define some attirbutes and functions inside of a class and crate another class
that can inherit all of those atttributes and functions
"""
from Chef import Chef# from <file> import <class>
from AsianChef import AsianChef# from <file> import <class>

# Press Shift+F10 to execute it or replace it with your code.

print('Chef:')
myChef = Chef()
myChef.make_special_dish()

print('Asian Chef:')
myAsianChef = AsianChef()
myAsianChef.make_special_dish()
myAsianChef.make_fried_rice()