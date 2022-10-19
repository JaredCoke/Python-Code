"""
Dictionary: a collection of Key-Value pairs that are Unordered and Mutable
"""

mydict = {"name":"Max","age":28,"city":'"New York'} #creates a dictionary
print(mydict, type(mydict))

mydict2 = dict(name="Max",age=28,city='"New York') #another way to create a dictionary
print(mydict2, type(mydict2))

#pass values from dictionary
try:
    value = mydict["ages"] #define what element you want to see by referenced KEY and NOT the exact element
    print('The requested value,',value, 'is a',type(value))
except KeyError:
    print('Ha - you encountered a Key Error. Youre looking for an element that doesnt exist in this list.\n')

###Editing Lists
mydict["email"] = "max@xyz.com" #Adds a value to the end of the list
print(mydict)
mydict["email"] = "waffles@xyz.com" #This overwrites the previous key
print(mydict)

#Deleting values from dictionaries
del mydict2["name"] #Deletes the called key-value pair; reference the key
print('A key-value pair was deleted',mydict2)


print(mydict2,"Another key-value pair was deleted with a keyed element = ",mydict2.pop("age")) #Deletes the called key-value pair and stores it for calling purposes
print("Yet another key-value pair was deleted.",mydict2.popitem(),'\n') #(Python 3.6 and below) = Removes an arbitary pair and (Python 3.7 and above) = Removes the last inserted pair

#check to see if an element exists in a dictionary
if "name" in mydict:
    print('The requested value exists in dictionary',mydict)
else:
    print("the value doesnst exist in this dicitonary.")

#another way to check to see if an element exists in a dictionary
try:
    print('The requested value',mydict["name"],'exists') #check to see if key exists;the value stored in the key is returned
except KeyError:
    print("The requested value doesnt appear in this list")

print('\n')

#Looping through dictionaries
for key in mydict:
    print(key) #This prints only the key. Not the value stored w/in

print('\n')

for key in mydict.keys():
    print(key) #This prints only the key. Not the value stored w/in

print('\n')

for value in mydict.values(): #The only way to call the values stored w/in the key
    print(value) #This prints only the value.

print('\n')

for key, value in mydict.items(): #request both the key and its value
    print(key,value) #This prints both the key and the value.

print('\n')

#Copying a dictionary
mydict_cpy = mydict #This way copies the dictionary, but also ties both dictionaries to the same data in our memory
mydict_cpy["email"] = "pancakes@xyz.com"
print('The original dictionary =',mydict)
print('The copied dictionary =',mydict_cpy)

mydict_cpy2 = mydict.copy() #This way copies the dictionary as two separate dictionaries
mydict_cpy2["email"] = "I CHANGED THIS"
print('The original dictionary =',mydict)
print('The copied dictionary =',mydict_cpy2)

mydict_cpy3 = dict(mydict) #Another way to copy the dictionary as two separate dictionaries
mydict_cpy3["email"] = "AGAIN it happened"
print('The original dictionary =',mydict)
print('The copied dictionary =',mydict_cpy3)

print('\n')


#Merging to dictionaries
my_dict = {"name":"Max","age":99,"email":"max@xyz.com"}
my_dict2 = dict(name="Senor",age="25",city="New York",additional="more values")

print('A new dictionary =',my_dict)
print('Another new dictionary = ',my_dict2)

my_dict.update(my_dict2) #stores another dictionary's key-value pairs into a dictionary; it overwrites what's there as well
print("The updated new dictionary =",my_dict2, '\n')


#Using other Key Types inside Dictionaries
my_dict3 = {3:6,6:36,9:81} #create a
print('A new dictionary filled with integers = ',my_dict3, "has data type =",type(my_dict3))

try:
    value = my_dict3[3] #searches for KEY requested; not value w/in key
    print("Congrats! The requested value",value, "does exist in dictionary")
except KeyError:
    print("Yo, you encountered a Key Error. The requested value doesn't exist in dictionary")

print('\n')

#
mytuple = (8,7) #create a tuple
mydict3 = {mytuple:15} #creates a dictionary from tuple. Key = tuple & Value = <defined value>
print('A tuple',mytuple, 'was created')
print('This dictionary', mydict3, "was created from a tuple \n")

#
mylist = ["food","book"] #creates a list
print(mylist)
try:
    mydict4 = {mylist:'test'} #It's not possible to create a dictionary from a list since a list can be changed after its creation. Setting a non-hashable key won't work
except TypeError:
    print("You encountered a TypError. It's not possible to create a dictionary from a list")
