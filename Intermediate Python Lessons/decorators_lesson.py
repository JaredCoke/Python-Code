"""
Decorators: A function that takes another function as an arguement and extends the behavior of this function w/o explicitly modifying it
- Function Decorators
- Class Decorators
"""

### [Function Decorator] Adds new functionality to an existing function
## Functions in Python are 1st class objects.They can be defined inside another function, passed as an arguement to another function, and returned from another function
# Default Syntax:
# @mydecorator
# def dosomething():
#     pass

## [Function Decorator] Example 1: Extending the Function of Another Function w/o Decorators
def start_end_decorator(func):

    def wrapper(): # inner function
        print('Start') # do something before the function
        func()
        print('End') # do something after the function
    return wrapper

def print_name():
    print('Jamal')

# print_name() # Simply prints 'Jamal'

print_name = start_end_decorator(print_name) # extend the function of 'print_name' to have other wrapper function
print_name() # prints the 'Start' & 'End' w/ the name


## [Function Decorator] Example 1a: Extending the Function of Another Function w/ Decorators
def start_end_decoratorA(func):

    def wrapperA(): # inner function
        print('Another Start') # do something before the function
        func()
        print('Another End') # do something after the function
    return wrapperA

@start_end_decorator # extend the function of 'print_name' to have other wrapper function
def print_nameA():
    print('Tyler')

# print_name() # Simply prints 'Jamal' if decorator wasn't there
print_nameA() # prints the 'Start' & 'End' w/ the name


print('\n')


## [Function Decorator] Example 2: Using Functions w/ Arguements
def start_end_decoratorB(func):

    def wrapperB(*args, **kwargs): # inner function | uses as many arguements & keywords as you want
        print('Beginning of Wrapper B') # do something before the function
        result = func(*args, **kwargs)
        print('End of Wrapper B') # do something after the function
        return result
    return wrapperB

@start_end_decoratorB # extend the function of 'print_name' to have other wrapper function
def add5(x):
    return x + 5

result = add5(10)
print(result)

print('')



## [Function Decorator] Example 2a: Using Functions w/ Arguements | Good Template !
import functools

def start_end_decoratorB1(func):

    @functools.wraps(func)
    def wrapperB1(*args, **kwargs): # inner function | uses as many arguements & keywords as you want
        print('Beginning of Wrapper B') # do something before the function
        result1 = func(*args, **kwargs)
        print('End of Wrapper B') # do something after the function
        return result1
    return wrapperB1

@start_end_decoratorB1 # extend the function of 'print_name' to have other wrapper function
def add5a(x1):
    return x1 + 5

print(help(add5a)) # show function identity
print(add5a.__name__) # shows name of the function

print('\n')

#############################################################################################
## [Function Decorator] Good Template ##
#############################################################################################
import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):  # inner function | uses as many arguements & keywords as you want
        # Do something before
        result = func(*args, **kwargs)
        # Do something after
        return result
    return wrapper

@my_decorator  # extend the function of below function to have other wrapper function
def add5(x):
    return x + 5
#############################################################################################


## [Function Decorator] Decorators w/ Arguements
import functools

def repeat(num_times): # outer function
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times): # start repeating
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3) # call the below function 3x
def greet(name):
    print(f'Hello {name}')

greet("Mam")

print('\n')


## [Function Decorator] Nested Decorators | Stacking decorators on top of each other
import functools


def start_end_decoratorC(func): # outer function

    @functools.wraps(func)
    def wrapperC(*args, **kwargs):
        print('Start')
        resultC = func(*args, **kwargs)
        print('End')
        return resultC
    return wrapperC

def debug(func): # this function extracts the name, the arguments, and keyword arguments - then prints the info
    @functools.wraps((func))
    def wrapperC1(*args, **kwargs): #extracts the name
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k,v in kwargs.items()]
        signature = ", ".join((args_repr + kwargs_repr))
        print(f"Calling {func.__name__}({signature}") # prints info
        resultC = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {resultC!r}") # prints info about the return value
        return resultC
    return wrapperC1

@debug
@start_end_decoratorC
def say_hello(name):
    greeting = f'Hello {name}'
    print(greeting)
    return greeting

say_hello("V3n0m") # decorators get called in the order they are listed

print('\n')




#############################################################################################
## [Class Decorator]  ## Behave Similar to Functin Decorators; Typically Used When You Want to Maintain & Update a State
#############################################################################################

## [Class Decorator] Example 1: Keep Track of How Many Times You've Called This Function
class CountCalls:

    def __init__(self,func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs): # same as init method in function decorators
        print('Well then - cya')

cc = CountCalls(None)
cc()

@CountCalls
def say_goodbye():
    print('Adios')

print('')


## [Class Decorator] Example 1a: Keep Track of How Many Times You've Called This Function
class CountCallsA:

    def __init__(self,funcA):
        self.func = funcA
        self.num_callsA = 0

    def __call__(self, *args, **kwargs): # same as init method in function decorators
        self.num_callsA += 1
        print(f"This has executed {self.num_callsA} times.")
        return self.func(*args, **kwargs)

@CountCallsA
def say_goodbyeA():
    print('Adios')

say_goodbyeA()
say_goodbyeA()