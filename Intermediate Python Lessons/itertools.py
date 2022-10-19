"""
Itertools: collection of tools handling iterators
Itertools: data types that can be used in a for loop.
Itertools consist of a product, permutations, combinations, accumulate, groupby, and/or infinite iterators.
*Most common itertools is a list.
"""

### PRODUCT = acts like a cross product
from itertools import product
a = [1,2]
b = [3,4]
prod = product(a,b)
print(prod) #default value doesn't show the elements
print("product =",list(prod)) #Use list method to see elements; uses cross product to combine element lists

a1 = [1,2]
b1 = [3]
prod1 = product(a1,b1, repeat=2)
print("product w/ repetition =",list(prod1)) #Use list method to see elements; uses cross product to combine element lists

print('\n')

### PERMUTATIONS = returns all possible orderings of an input
from itertools import permutations
a = [1,2,3]
perm = permutations(a)
print(perm)
print("Permutations =",list(perm))

perm1 = permutations(a,2)
print("Only Permutations that contain 2 digits =",list(perm1))

print('\n')

### Combinations = will make all possible combinations w/ a specified length
from itertools import combinations
a = [1,2,3,4]
comb = combinations(a,2) #creates 2 element combinations
print(list(comb))

# Show combinations with the same element
from itertools import combinations, combinations_with_replacement
a = [1,2,3,4]
comb_wr = combinations_with_replacement(a,2) #allows you to see 2 element combinations with the same element type
print(list(comb_wr))

print('\n')

### Accumulate = iterator that returns accumalated sums, or any other binary function defined as an input
from itertools import accumulate
a = [1,2,3,4]
acc = accumulate(a) #default functions will compute the sums
print(a)
print("The default sum accumulation =",list(acc))

#changing the accumation operators
from itertools import accumulate
import operator
a1 = [2,2,2,2]
acc1 = accumulate(a1, func=operator.mul) #calling multiplication on elements; element times
print(a1)
print("The multiplication accumulation =",list(acc1)) # returns the first element then that element times the next element, etc

#using the max comparision
from itertools import accumulate
import operator
a2 = [1,2,5,3,4]
acc2 = accumulate(a2, func=max) #returns the max of the elements as it indexes through the list
print(a2)
print("The max accumulation =",list(acc2)) #it holds the hiighest eleement found until the list is complete

print('\n')


### groupby = makes an iterator that returns keys and groups from an iterable
from itertools import groupby

def smaller_than_3(x): #create a quick function to use
    return x < 3

a1 = [1,2,3,4]
group_obj = groupby(a1, key=smaller_than_3) # groups all values together that are smaller than 3, and ones that aren't differently
print(group_obj)
print("The groupby group_obj =",list(group_obj)) #still doesn't show the value elements, only the keys are shown

#Accessing the value elements
a1a = [1,2,3,4]
group_obj = groupby(a1a, key=smaller_than_3) # groups all values together that are smaller than 3, and ones that aren't differently
for key, value in group_obj:
    print("key =",key,",value =",list(value))

#using a lambda function
a2 = [1,2,3,4]
group_obj = groupby(a, key=lambda x: x<3) #use lambda function (small 1 line function that has an input and can do some expression to return an output)
for key, value in group_obj:
    print("Using lambda function key =",key,",Using lambda function value =",list(value))

print('')

#grouping the people w/ similar ages
persons = [{"name":"Jamal","age":25},{"name":"Wendell","age":25},{"name":"San","age":23},{"name":"Tyler","age":19}] #create a list full of dictionaries

group_obj = groupby(persons, key=lambda x: x["age"]) #lambda function to group adjacent elements with similar ages
for key, value in group_obj:
    print("Using lambda function key =",key,",Using lambda function value =",list(value))

print('\n')


###Infinit Iterables = count, cycle, and repeat functions
# Count = counts indefinitely at the specified starting value
from itertools import count

for i in count(10): #count(10) starts counting at 10
    print("Count iterable: i =",i)
    if i == 15:
        break #this stops the infinite count loop

#Cycle = cycles infinitely thorough an iterable
from itertools import cycle

a = [1,2,3]
for i in cycle(a): #cycles through list and then repeats indefinitely; use a crafty break statement to escape
    print("Cycles: i =",i)
    if i == 3:
        break


#Repeat = cycles infinitely through an iterable
from itertools import repeat

a = [1,2,3]
for i in repeat(a): #repeats list indefinitely; use a crafty break statement to escape
    print("Repeat: i =",i)
    if i == a: #if i = list, escape
        break

#repeat w/ arguements
a = [1, 2, 3]
for i in repeat(a,4):  #repeats list 4 times
    print("Repeat: i w/ arguements=", i)
