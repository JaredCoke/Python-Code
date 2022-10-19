"""
Collections: implements special container data types: Counter, namedtuple, OrderedDict, defaultdict, deque
"""

### Counter = a container that stores elements as dictionary keys and their counts as dictionary values.

from collections import Counter
a = "aaaaabbbccccccc"
my_counter = Counter(a) #converts string to a dictionary that counts the duplicate
print('my_counter = ',my_counter)
print('my_counter.items() =',my_counter.items()) # shows the key value pairs
print('my_counter.keys() =',my_counter.keys()) # shows the key pairs
print('my_counter.values() =',my_counter.values()) # shows the key pairs

print('')
print('my_counter.most_common(1) =',my_counter.most_common(1)) # shows the element with the largest counter | repeats the most; returns a list w/ tuples
print('my_counter.most_commo2ndn(2) =',my_counter.most_common(2)) # shows the top 2 most common counters; returns a list w/ tuples
print('my_counter.most_common(1)[0] =',my_counter.most_common(1)[0]) # shows the first most common key value pairs
print('my_counter.most_common(1)[0][0] =',my_counter.most_common(1)[0][0]) # shows the first most common key value pairs's element

print('my_counter.list(elements()) =',list(my_counter.elements())) #turns stringed dictionary into a list
print('\n')


### namedtuples = easy to create lightweight object type (similar to a struct)
from collections import namedtuple
Point = namedtuple('Point','x,y') #creates a 2D point; format = namedtuple('Class','arguement1,arguement2')
pt = Point(1,-4)
print('pt =',pt)
print('pt.x =',pt.x,'pt.y =',pt.y) #accesses tuple elements only


### OrderedDict = a regular dictionary, but it remembers the sequence the numbers were defined; obsolete since Python 3.7+
from collections import OrderedDict
ordered_dict = OrderedDict() #creates an ordered dictionary; only necessary in Pyton 3.6-
ordered_dict['a'] = 9
ordered_dict['b'] = 3
ordered_dict['c'] = 5
ordered_dict['d'] = 6
print('OrderedDict method =',ordered_dict)

reg_dict = {} #creates a dictionary normally
reg_dict['a'] = 9
reg_dict['b'] = 3
reg_dict['c'] = 5
reg_dict['d'] = 6
print('Normal dictionary method =',reg_dict)

print('\n')

### defaultdict = similar to regular dictionary container, w/ a difference that it will have a default value if the key hasn't been set yet
from collections import defaultdict
d1 = defaultdict(int) #creates a dictionary w/ data type integer
d1['a'] = 1
d1['b'] = 3
print('d1 =',d1) #Returns the class type and entire dicionary

d2 = defaultdict(float) #creates a dictionary w/ data type float
d2['a'] = 1
d2['b'] = 3
print('d2 =',d2) #Returns the class type and entire dicionary

d3 = defaultdict(str) #creates a dictionary w/ data type string
d3['a'] = 1
d3['b'] = 3
print('d3 =',d3) #Returns the class type and entire dicionary

print('')

print("d1['a'] =",d1['a']) #returns the value for the specified element
print("d1['b'] =",d1['b'])
print("Non-existent value, d1['c'] =",d1['c']) #if requested value doesn't exist - returns a 0

print('')

d4 = defaultdict(list) #creates a dictionary w/ data type 'list'
d4['a'] = 1
d4['b'] = 3
print('d4 =',d4) #Returns the class type and entire dicionary
print("Non-existent value, d4['c'] =",d4['c']) #if requested value doesn't exist - returns an empty list

d4a = {}
d4a['a'] = 1
d4a['b'] = 3

try:
    print("Non-existent value, d4a['c'] =",d4a['c']) #if requested value doesn't exist - returns an empty list
except KeyError:
    print("Non-existent value, d4a['c'] = 3 throws an error! \n since it wasn't created using a default dictionary.")

print('\n')

### deque = double ended queue which can be used to add or remove elements from both ends (very efficiently)
from collections import deque

deque_var = deque()

deque_var.append(1)
deque_var.append(2)
print("deque_var =",deque_var)
print("It has a data type =",type(deque_var))

deque_var.appendleft(7) #adds element to beginning of the deque
print("modified appended deque_var =",deque_var)

deque_var.pop() #removes the last element
print("modified popped deque_var =",deque_var)
deque_var.popleft() #removes the first element
print("modified popped left deque_var =",deque_var)

deque_var.clear() #wipes the entire deque out
print("modified wiped deque_var =",deque_var)

deque_var.extend([33,44,55]) #adds multiple elements to the entire deque
print("modified extended deque_var =",deque_var)
deque_var.extendleft([11,22,33]) #adds multiple elements to the entire deque from the left in right to left order
print("modified left extended deque_var =",deque_var)

print('')

deque_var1 = deque([1,2,3,4]) #create a new deques
print("deque_var1 =",deque_var1)
deque_var1.rotate(1) #shifts every element over by one space to the right; last element moves to beginning of deque
print("right shifted rotated deque_var1 =",deque_var1)
deque_var1 = deque([1,2,3,4]) #recreates the original deque
deque_var1.rotate(-1) #shifts every element over by one space to the left; last element moves to beginning of deque
print("left shifted rotated deque_var1 =",deque_var1)
