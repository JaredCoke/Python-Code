"""
Generators: Functions that return an object that can be iteratred over.
Generators: return the object lazily; generate items only one at a time and only when you ask for it. Best for memory efficient purposes - especially w/ large data sets.
Powerful advanced Python technique.
-
-
"""

### [Generator] Example 1: Basic Generator Function; Returning Eveery Element

def mygenerator():
    yield 1
    yield 2
    yield 3

g = mygenerator()

print(g) # prints the generator object | all metadata

for element in g: # prints all elements inside mygenerator
    print(element)

print('')


### [Generator] Example 1a: Basic Generator Function; Using Next Function to Return Values One At a Time

def mygeneratorA():
    yield 1
    yield 2
    yield 3

gA = mygeneratorA()

print(gA) # prints the generator object | all metadata

valueA = next(gA) # use the next function to return values one at a time and stops at yield statement
print(valueA)
valueA = next(gA) # use the next function to return the next value
print(valueA)
valueA = next(gA) # use the next function to return the next value
print(valueA)
try:
    valueA = next(gA) # use the next function to attempt to return the next value
    print(valueA)
except:
    print("Ha. You encountered a StopIteration")

print('')


### [Generator] Example 1b: Basic Generator Function; Using Sum Function
# Using generators as inputs to other Functions

def mygeneratorB():
    yield 1
    yield 2
    yield 3

gB = mygeneratorB()

print(sum(gB)) # returns the sum of every element

print('')


### [Generator] Example 1c: Basic Generator Function; Using Sorted Function
# Using generators as inputs to other Functions

def mygeneratorC():
    yield 3
    yield 2
    yield 1

gC = mygeneratorC()

print(sorted(gC)) # returns the elements as a list w/ everything sorted

print('\n')

### [Executing Generators] Example 2: Execution of a Generator Function
#

def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1

cd = countdown(4) # this does not call the function; only defines it

value2 = next(cd) # runs until it reaches the first yield statement and then stops
print("The first value2's element =",value2) # returns the starting value/element

value2 = next(cd) # runs until it reaches the next yield statement and then stops
print("The next value2's element =",value2) # returns the next value/element

value2 = next(cd) # runs until it reaches the next yield statement and then stops
print("The next value2's element =",value2) # returns the next value/element

value2 = next(cd) # runs until it reaches the next yield statement and then stops
print("The next value2's element =",value2) # returns the next value/element

for element in cd:
    try:
        value2 = next(cd)  # runs until it reaches the next yield statement and then stops
        print("The next value2's element =", element)  # returns the next value/element
    except:
        print("Ha. You encountered a StopIteration")

print('')

### [Executing Generators] Example 2.1: Execution of a Generator Function
#

def countdown1(num1):
    print('Starting')
    while num1 > 0:
        yield num1
        num1 -= 1

cd1 = countdown1(4) # this does not call the function; only defines it


for element1 in cd1: # loop thru the elements until it fails
    try:
        print("The next value2's element =", element1)  # returns the next value/element
    except:
        print("Ha. You encountered a StopIteration")

print('\n')


### [Memory Efficient Generators] Counting Up to Number
import sys

# Non-Memory Efficient Way !!! Takes Too Much Memory
def firstn(n): # define a function to take a number from 0-n as an input and then return a sequence w/ all of the numbers.
    nums = [] # create a list | stores every value in list during an iteration
    num = 0
    while num < n:
        nums.append(num)
        num += 1 # adds 1 to 'num' value
    return nums

# Memory Efficient Way.
def firstn_generator(n): # doesn't have to save all of the elements in an array
    num = 0
    while num < n:
        yield num
        num+= 1

print(f"nums list = {firstn(10)}") # all of the elements are stored in list 'nums'
print(f"nums list sum = {sum(firstn(10))}")
print(sys.getsizeof(firstn(10)))

#print(f"nums list = {firstn_generator(10)}") # all of the elements are stored in list 'nums'
print(f"Memory efficient sum = {sum(firstn_generator(10))}")
print(sys.getsizeof(firstn_generator(10)))

print('')



### [Memory Efficient Generators] Counting Up to Number | Scaling Up Number
import sys

# Non-Memory Efficient Way !!! Takes Too Much Memory
def firstn1(n1): # define a function to take a number from 0-n as an input and then return a sequence w/ all of the numbers.
    nums1 = [] # create a list | stores every value in list during an iteration
    num1 = 0
    while num1 < n1:
        nums1.append(num1)
        num1 += 1 # adds 1 to 'num' value
    return nums1

# Memory Efficient Way.
def firstn_generator1(n1): # doesn't have to save all of the elements in an array
    num1 = 0
    while num1 < n1:
        yield num1
        num1+= 1

print(f"nums list sum = {sum(firstn1(1000000))}")
print("firstn Memory size w/ a list =",sys.getsizeof(firstn1(1000000)))

print(f"Memory efficient sum = {sum(firstn_generator1(1000000))}")
print("firstn_generator Memory size w/o a list =",sys.getsizeof(firstn_generator1(1000000)))



### [Generators] Using Fibonacci Sequence in Generators

def fibonacci(limit):
    # sequence: 0 1 1 2 3 5 8 13 ...
    a, b = 0,1
    while a < limit:
        yield a
        a, b = b, a + b

fib = fibonacci(30)

for element in fib:
    print(element)

print('\n')


### [Generators] Generator Expressions

mygenerator = (i for i in range(10) if i %2 == 0)
for i in mygenerator: # returns elements one at a time
    print(i)

# using list comprehension
mygenerator = [i for i in range(10) if i %2 == 0] # returns numbers as a list
print(mygenerator)

# convert set to a list
mygenerator3 = (i for i in range(10) if i %2 == 0)
print(list(mygenerator3))


### [Generators] Generator Expressions w/ Size Counts
import sys

mygenerator4 = (i for i in range(1000000) if i %2 == 0)
print(sys.getsizeof(mygenerator4)) # waaaaaay smaller

# using list comprehension
mylist = [i for i in range(1000000) if i %2 == 0] # returns numbers as a list
print(sys.getsizeof(mylist))
