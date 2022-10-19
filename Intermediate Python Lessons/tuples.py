"""
Tuples = ordered, imutable,collection of data which allows duplicate elements. Can't be changed after its creation
Often used for objects that belong together
"""

mytuple = ("Max",28, "Boston")
print(mytuple, type(mytuple))

mytuple = "Max",32, "Boston" #alternate way to define a tuple
print(mytuple, type(mytuple))

mytuple = tuple(["Max",99,"Boston"]) #another alternatte way to define a tuple
print(mytuple, type(mytuple))

mytuple2 = ("Max") #this creates a string; not a tuple
print(mytuple2,type(mytuple2))
mytuple2_fixed = ("Max",) #this creates a tuple with only one element
print(mytuple2_fixed, type(mytuple2_fixed), '\n')

item = mytuple[0] #accessing elements
print('The first element is ',item)
item = mytuple[-1] #access the last element
print('The last elemnt is ',item)

### Attempt to change a tuple triggers a TypeError
try:
    mytuple[0] = "Waffles"
except TypeError:
    print('D-oh. You encountered a TypeError. You tried to change an immutable object: ', type(mytuple),'\n')

#print all elements in the tuple
for x in mytuple:
    print(x)

#check to see if element exists in tuple
element = 'Max'
if element in mytuple:
    print('Yes!', element, 'exists in our tuple.')
else:
    print('No!', element,'does not exist.')


mytuple3 = ('a','p','p','l','e')
print('There are',len(mytuple3), 'elements in this tuple.') # check length of tuple elements
print('There are',mytuple3.count('p'), 'p in this tuple') #counts the requested element's number of element occurences
print('Element l has an index of',mytuple3.index('l'), '\n')

#Converting tuples to lists and vice-versa
my_list = list(mytuple)
print(my_list, 'Is the list converted from mytuple. It has a datatype of',type(my_list))
my_tuple_from_my_list = tuple(my_list)
print(my_tuple_from_my_list,'Is the tuple converted from my_list. It has a datatype of',type(my_tuple_from_my_list),'\n')

#slicing tuples
a = (1,2,3,4,5,6,7)
b = a[0:7] # This stores all elements from beginning to one more than the last element(to get everything)
c = a[:7] # Another way to store everything. This returns everything until the index specified
d = a[0:] #Another way to store everything
e = a[::] #Another way to store everything
f = a[0:7:3] #This stores every 3rd index starting from index 0
g = a[::3] #This stores every 3rd index starting from index 0
h = a[::-1] #This reverses your tuple
i = a[::-3] #This stores every 3rd element from the back-forward your tuple
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i,'\n')

#unpacking
mytuple4 = "Waffles", 9, 'tequila'
name, age, drink = mytuple4 #matching the elements to the indices
print(name,age,drink,'\n')

mytuple5 = (1,2,3,4,5,6)
i1, *i2, i3 = mytuple5 # This *i2 grabs all of the elements that are between the other values
print('The first index element is ',i1)
print('The last index element is ',i3)
print('All of the values between the first and last index are ',*i2, '\n')

#Working with a tuple can be more efficient sometimes w/ large data since a tuple is immutable
import sys
my_list_for_comparision = [0, 1, 2, "hello", True]
my_tuple_for_comparision = (0, 1, 2, "hello", True)
print('The size of my list is',sys.getsizeof(my_list_for_comparision)) #get size of list
print('The size of my tuple is',sys.getsizeof(my_tuple_for_comparision),'\n') #get size of tuple

#It can be more efficient to iterate over a tuple, especially when comparing time it takes to handle/create the different datatypes
import timeit
print('The timee it takes to create a list =',timeit.timeit(stmt="[0,1,2,3,4,5]",number=1000000)) #check time it takes to create a list 1million times
print('The time it takes to create a tuple =',timeit.timeit(stmt="(0,1,2,3,4,5)",number=1000000)) #check time it takes to create a tuple 1million times