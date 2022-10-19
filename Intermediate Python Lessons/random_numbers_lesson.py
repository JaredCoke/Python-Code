"""
Random Numbers:
- random module = pseudo random numbers
- secrets module = cryptographically strong random numbers
- NumPy random = generate arrays w/ random numbers
"""

### [Random Module] Generate pseudo random for various distributions; these numbers are reproducible
import random

a = random.random() # prints a random float in the range of 0 to 1
print("The random.random() =",a)

a1 = random.uniform(1,10) # prints a random float in the range of 1 to 10
print("The random.uniform(1,10) =",a1)

a1a = random.randint(1,10) # prints a random int in the range of 1 to 10; this does include the upper bound '10' to be generated
print("The random.randint(1,10) =",a1a)

a1b = random.randrange(1,10) # prints a random int in the range of 1 to 10; this does NOT include the upper bound '10' to be generated
print("The random.randrange(1,10) =",a1b)

print('')


## Random Variate Function
import random

a2 = random.normalvariate(0,1) # picks a random value from a normal distribution w/ a mean of 0 and the standard deviation of 1
print("The random.normalvariate =",a2)

mylist = list('ABCDEFG')
print("mylist =",mylist)
a2a = random.choice(mylist)
print("A random choice from mylist =",a2a)

## Random Samples
mylist = list('ABCDEFG')
a2b = random.sample(mylist, 3) # returns 3 random elements from mylist; only picks unique elements | never same value twice
print("3 Random Samples =",a2b)

## Random Choices
mylist = list('ABCDEFG')
a2c = random.choices(mylist, k=3) # returns 3 random elements from mylist; can pick same element multiple times
print("3 Random Choices =",a2c)

## Random Shuffle
import random

mylist = list('ABCDEFG')
random.shuffle(mylist) # shuffles the entire list of elements amongst the indices
print(mylist)

print('\n')


##Reproduce Random values
import random

random.seed(1)
print(random.random())
print(random.randint(1,10))
random.seed(1)
print(random.random()) # The same values from above are seen here
print(random.randint(1,10)) # The same values from above are seen here

print('')

##Reproduce Random values w/ Different Seeds
import random

random.seed(1)
print(random.random())
print(random.randint(1,10))
random.seed(2)
print(random.random())
print(random.randint(1,10))

random.seed(1)
print(random.random())
print(random.randint(1,10))
random.seed(2)
print(random.random())
print(random.randint(1,10))



### [] Secrets Module
import secrets

b = secrets.randbelow(10) # generate a random integer from 0 - 10, not including the upper bound '10'
print("secrets.randbelow =",b)
b1 = secrets.randbits(4) # returns a random int w/ k bytes | 4 different random binary values
print("secrets.randbits =",b1)
mylistB = list("ABCDEFG")
b1a = secrets.choice(mylist)
print("secrets.choice = ",b1a)

print('\n')

### NumPy
import numpy as np

c = np.random.rand(3) # creates a 1D array w/ 3 random floats elements
print("numpy random array w/ 3 elements =",c)

c = np.random.rand(3,3) # creates a 1D array w/ 3 random floats elements
print("numpy random array w/ 3 elements =",c)

c = np.random.randint(0,10,3) # creates a 1D array w/ 3 random floats elements
print("numpy random array w/ 3 elements =",c)

c = np.random.randint(0,10,(3,4)) # creates a 1D array w/ 3 random floats elements
print("numpy random array w/ 3 elements =",c)

print('')



## Random Array w/ different dimensions
import numpy as np

arr = np.array([1,2,3],[4,5,6])
print(arr)
np.random.shuffle(arr)
print("shuffled =",arr)


## Random Numpy Seeds
import numpy as np

np.random.seed(1)
print(np.random.rand(3,3))
np.random.seed(1)
print(np.random.rand(3,3))
