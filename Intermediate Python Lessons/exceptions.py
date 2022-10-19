"""
Errors & Exceptions
"""

# Syntax Error = parser detects a syntactically incorrect statement
# a = 5 print(a)
# OR
# a = 5
# print(a))

### Exception = a syntactically correct statement that throws an error when executed
# [Exception] type error
# a = 5 + 'waffles' # throws a type error

# [Exception] import error
# import somemodule # module doesn't exist; import error

# [Exception] name error
# a = 5
# b = c # c is not defined; name error

# [Exception] file not found error
# f = open('somefile.txt') #file doesn't exist

# [Exception] value error
# a = [1,2,3]
# a.remove(4) # element doesn't exist in list

# [Exception] index error
# a = [1,2,3]
# a[4] # element doesn't exist and can't be indexed

# [Exception] key error
# my_dict = {'name':'Manny'}
# my_dict['age'] # key 'age' doesn't exist in dictionary



### Raising an Exception = forcing an exception to occur when otherwise it wouldn't
# x = -5
# if x < 0:
#     raise Exception('x should be positive') # stops code from executing by creating an exception
# print('oh yeah') # this phrase doesn't get executed

# [Raising an Exception] assertion error = throws an assertion error if your assertion is not true
# x = -5
# assert (x >= 0) # assert statement

# [Raising an Exception] Another assertion error = throws an assertion error if your assertion is not true
# x = -5
# assert (x >= 0), 'x is not positive' # assert statement that prints out a message



### Handling Exceptions: catch exceptions w/ a try-except block

# [Handling Exception] basic try-except block
try:
    a = 5/0 # throws a ZeroDivisionError
except:
    print('Uh oh. You threw a ZeroDivisionError')

# [Handling Exception] storing try-except block
try:
    a = 5/0 # throws a ZeroDivisionError
except Exception as error_type: # stores the error type as any variable
    print(f'Uh oh. You threw a {error_type}')

# [Handling Exception] better try-except block
try:
    a = 5/0 # throws a ZeroDivisionError
except ZeroDivisionError: # only executes this error case if it's a ZeroDivisionError
    print('Uh oh. You threw a ZeroDivisionError')

# [Handling Exception] Multiple try-except block
try:
    a = 5/1
    b = a + '10'
except ZeroDivisionError as error_type: # only executes this error case if its a ZeroDivisionError
    print(f'Uh oh. You threw a {error_type}')
except TypeError as error_type: # only executes this error case if its a TypeError
    print(f"Uh oh. You threw a '{error_type}'")

# [Handling Exception] Adding an else clause
try:
    a = 5 / 1
    b = a + 10
except ZeroDivisionError as error_type:  # only executes this error case if its a ZeroDivisionError
    print(f'Uh oh. You threw a {error_type}')
except TypeError as error_type:  # only executes this error case if its a TypeError
    print(f"Uh oh. You threw a '{error_type}'")
else:
    print('No errors occurred.... for now....') # prints this if no errors were encountered

print('')

# [Handling Exception] Adding a finally clause
try:
    a = 5 / 1
    b = a + '10'
except ZeroDivisionError as error_type:  # only executes this error case if its a ZeroDivisionError
    print(f'Uh oh. You threw a {error_type}')
except TypeError as error_type:  # only executes this error case if its a TypeError
    print(f"Uh oh. You threw a '{error_type}'")
else:
    print('No errors occurred.... for now....')  # prints this if no errors were encountered
finally:
    print('This is the finally clause') # this gets executed regardless of any errors or else statments


print('\n')



# [Defining Custom Exception] Define your own exceptions by subclassing from a class

# [Defining Custom Exception] basic version: Define your own exceptions by subclassing from the base exception class
class ValueTooHighError(Exception): # call an already created class
    pass

def test_value(x): # creates a new exception error
    if x > 100:
        raise ValueTooHighError('value is too high')

try:
    test_value(200)
except ValueTooHighError as error_type:
    print("Custom Error Exception: ",error_type)

print('')

# [Defining Custom Exception] two classes
class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception): # define a new class
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(x): # creates a new exception error
    if x > 100:
        raise ValueTooHighError('value is too high.')
    if x < 5:
        raise ValueTooSmallError('value is too small.',x) # returns statement and specified element

try:
    test_value(1)
except ValueTooHighError as error_type:
    print("Custom Error Exception: ",error_type)
except ValueTooSmallError as error_type:
    print("Custom Error Exception: ", error_type) # prints the specified message together

print('')

# [Defining Custom Exception] More data w/ two classes
class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception): # define a new class
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(x): # creates a new exception error
    if x > 100:
        raise ValueTooHighError('value is too high.')
    if x < 5:
        raise ValueTooSmallError('value is too small.',x) # returns statement and specified element

try:
    test_value(1)
except ValueTooHighError as error_type:
    print("Custom Error Exception: ",error_type)
except ValueTooSmallError as error_type:
    print("Custom Error Exception: ", error_type.message, error_type.value) # prints the specified element separately