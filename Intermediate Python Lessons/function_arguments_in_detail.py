"""
- The difference between arguments and parameters
- Positional and keyword arguments
- Default arguments
- Variable-length arguments (*args and **kwargs)
- Container unpacking into function arguments
- Local vs. global arguments
- Parameter passing (by value or by reference)
"""

### [Types of Args & Params] The difference between arguments and parameters
# parameters = defined or used inside parentheses where defining a function
# arguments = values passed for these parameters while calling a function

def print_name(name): # name = parameter
    print(name)

print_name('waffles') # 'waffles' = argument

print('')

## [Types of Args & Params] Example 2: Positional Arguments
def foo(a,b,c): # defining a function w/ Positional Arguments
    print(f"a= {a} b={b} c={c}")

foo(1, 2, 3) # passing arguments as postional arguments

print('')

## [Types of Args & Params] Example 2a: Keyword Arguments
def foo1(a,b,c): # defining a function w/ Positional Arguments
    print(f"a= {a} b={b} c={c}")

foo1(a=1, b=2, c=3) # passing arguments as keyword arguments
foo1(c=1, a=2, b=3) # passing arguments as keyword arguments | the order is not important


print('')

## [Types of Args & Params] Example 2b: Combo of Positional & Keyword Arguments
def foo2(a,b,c): # defining a function w/ Positional Arguments
    print(f"a= {a} b={b} c={c}")

foo2(1, b=2, c=3) # passing arguments as paremeters & keyword arguments
# foo2(1, b=2, 3) # Sytnax Error: passing arguments as paremeters & keyword arguments AND switching back to parameters
# foo2(1, a=2, c=3) # Type Error: passing arguments into the same variable using paremeters & keyword arguments
# best to use keyword arguments for readabiltiy and order-agnostic
print('')


## [Types of Args & Params] Example 2c: Adding Default Arguments
def foo3(a,b,c, d=4): # defining a function w/ Positional Arguments & a Default arguments | All default params must be at the end of the function
    print(f"a= {a} b={b} c={c} d={d}")

foo3(1, 2, 3) # passing arguments as paremeters w/o calling default argument 'd' and it still prints it
foo3(1, 2, 3, 12) # changing value of 'd'

def foo3a(a,b,c, d=4, e=45): # defining a function w/ Positional Arguments & a Default arguments | All default params must be at the end of the function
    print(f"a= {a} b={b} c={c} d={d}, e={e}")

foo3a(1, 2, 3)
print('\n')



########################################################################################################
### [Variable Length] Example 3: Variable Length Arguments
########################################################################################################
def waffle(a,b,*args, **kwargs): #
    # marking a paraemeter w/ one '*' then you can pass any number of positional arguments to your function | typically called args (you can rename)
    # marking a paraemeter w/ two '**' then you can pass any number of keyword arguments to your function | typically called kwargs (you can rename)
    print(f"a= {a} b={b}")
    for arg in args: # Note: 'arg' parameter is a tuple
        print(arg)
    for key in kwargs: # Note: 'kwargs' keyword is a dictionary
        print(key,kwargs[key])


waffle(1, 2, 3, 4, 5, six = 6, food = 'waffle') # passing unlimited arguments as parameters and keyword arguments

print('')


## [Types of Args & Params] Example 3a: Force Keyword Arguments | when you want to have keyword only arguments
def waffleA(a,b,*, c,d): # forcing keyword arguments
    print(f"a= {a} b={b} c={c} d={d}")

# waffleA(1, 2, 3, 4) # TypeError: this function only takes 2 positional arguments; the rest must be keyword arguments
waffleA(1, 2, c = 3, d = 4) # passing all arguments after b as keywords

print('')


## [Types of Args & Params] Example 3b: Force Keyword Arguments | when you want to have keyword only arguments
def waffleB(*args, last): # forcing keyword arguments
    for arg in args:
        print(arg)
    print(last)

# waffleB(1, 2, 3) # TypeError: waffleB is missing the 'last' keyword
waffleB(1,2,3, last=100) # enforcing keyword only arguments

print('\n')



########################################################################################################
### [Container Arguments] Example 4: Container unpacking into function arguments
########################################################################################################
def container_example(a,b,c):
    print(f"List Container example: a= {a} b={b} c={c}")

my_list = [0,1,2] # define a list as a container
container_example(*my_list) # unpack the list into the function

print('')

def container_exampleA(a,b,c):
    print(f"Tuple Container example: a= {a} b={b} c={c}")

my_tuple = (0,1,2) # define a tuple as a container | length of the container must match the length of the arguments
container_exampleA(*my_tuple) # unpack the list into the function

print('')

def container_exampleA(a,b,c):
    print(f"Dictionary Container example: a= {a} b={b} c={c}")

my_dict = {'a':0,'b':1,'c':2} # define a dictionary as a container | length of the container must match the length of the arguments | variables must match the variables exactly as defined in function
container_exampleA(**my_dict) # unpack the list into the function


print('\n')



########################################################################################################
### [Local & Gloabl Arguments] Example 5: Local vs. global arguments
########################################################################################################
#  local vs global variables

# local variable inside function
def my_function():
    x = number # define new local variable
    print('number inside function:',x)


number = 0 # define a global variable
my_function()
print(number)


# modifying global variable inside function
def my_functionA():
    global numberA
    xA = numberA # define local variable
    numberA = 3
    print('number inside function:',xA)


numberA = 0 # define a global variable
my_functionA()
print('Global number after funtion =',numberA)




print('\n')



########################################################################################################
### [Parameter Passing] Example 5: Parameter Passing (by value or by reference)
########################################################################################################
# Call by Value or Call by Reference = [Python] Call by Object OR Call by Object Reference

# Mutable Objects (lists, dictionaries) can be changed w/in a method
# If you rebind the reference (list/dictionaries) in the method - then the outer reference will still point to the original object and is not changed

# Immutable Objects (integers, strings) can't be changed w/in a method
# Immutable objects contained w/in a mutable object can be reassigned w/in a method

print('Beginning Parameter Passing:')

def parameter_passing(x):
    x = 5 # creates a local variable

var = 10 # immutable variable, integer
parameter_passing(var)
print(var)

print('')

# Mutable Object Passing
def parameter_passing1(a_list):
    a_list.append(4)

my_list1 = [1,2,3] # mutable variable, list
parameter_passing1(my_list1)
print(my_list1)


print('')

# Changing Integers w/in a List | Mutable Object Passing
def parameter_passing2(a_list):
    a_list.append(4)
    a_list[0] = -100 # changing the first index

my_list2 = [1,2,3] # mutable variable, list
parameter_passing2(my_list2)
print(my_list2)

print('')

# The outer reference will NOT be changed | Mutable Object Passing
def parameter_passing3(a_list):
    a_list = [100, 200, 300] # define a local variable, list
    a_list.append(4)
    a_list[0] = -100 # changing the first index

my_list3 = [1,2,3] # mutable variable, list | global list that doesn't change once function is executed
parameter_passing3(my_list2)
print(my_list3)


print('')

# The outer reference will be Appended | Mutable Object Passing
def parameter_passing3a(a_list):
    a_list += [100, 200, 300] # appends local variable, list to global variable
    a_list.append(4)
    a_list[0] = -100 # changing the first index

my_list3a = [1,2,3] # mutable variable, list | global list that doesn't change once function is executed
parameter_passing3a(my_list3a)
print(my_list3a)


print('')

# The outer reference will NOT be changed | Mutable Object Passing
def parameter_passing3b(a_list):
    a_list = a_list + [100, 200, 300] # define a local variable, list | does not modify global variable
    a_list.append(4)
    a_list[0] = -100 # changing the first index

my_list3b = [1,2,3] # mutable variable, list | global list that doesn't change once function is executed
parameter_passing3b(my_list3b)
print(my_list3b)