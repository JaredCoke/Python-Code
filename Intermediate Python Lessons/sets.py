"""
Sets: collection datatype that is unordered, mutable, but contain no duplicates
"""

### CREATE A SET ###
myset = {1,2,3} #Creates a set
print(myset)

myset2 = {1,2,3,1,2} #Creates a set; doesn't store the duplicate data
print(myset2)

myset3 = set([1,2,3]) #Another way to create a set
print(myset3)

myset4 = set("Waffles") #Creates a set from strings; doesn't store the duplicate letters; maintains the letters in an arbitrary order
print(myset4) #Letters are printed in a random/arbitrary order

myset5a = {} #Incorrectly attempts to create a set; creates a dicitonary instead
myset5 = set() # The only way to create an empty set
print("myset5a = {} only defines a",type(myset5a),"filled with",myset5a)
print("myset5 = set() creates a",type(myset5),"filled with",myset5)


### MODIFYING SET DATA ###
myset5.add(1)
myset5.add(2)
myset5.add(3)
print(myset5)

try:
    myset5.remove(4) #Removes an element. Throws an error if the element doesn't exist.
    print(myset5)
except KeyError:
    print("Uh oh. You have a KeyError. THe element you want to delete doesn't exist in this set.")

myset5.discard(1) #Removes an element. No error is thrown if it doesn't exist.
print(myset5)

myset4.clear() #This clears all data in the set
print(myset4)

popped_off_value = myset5.pop() #Returns and Deletes arbitrary(or only first?) element in the set
print('The popped off value is', popped_off_value, "from set", myset5)

print('\n')

###CALLING DATA IN SETS
for element in myset:
    print(element)

element = 'w'
if element in myset:
    print('The requested value',element, 'exist in this set.')
else:
    print("The requested value",element,"doesn't exist in this set")

print('\n')

### UNIONS ###
#combines elements from two sets w/o duplication

odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7}

print("Odd set =",odds)
print("Even set =",evens)
print("Prime set =",primes)

u = odds.union(evens) #combines the two sets in order
print("The union of odds and evens =",u)
print("The unchanged Odd set =",odds)
print("The unchanged Even set =",evens,'\n')

###INTERSECTION###
#Takes elements that are found in both sets; shows duplicates

d = odds.intersection(primes) #show duplicate elements
d1 = odds.intersection(evens) #will create an empty set if no duplicates found
print("The intersection of odds and primes =",d)
print("The intersection of odds and evens =",d1)
print("The unchanged Odd set =",odds)
print("The unchanged Even set =",evens)
print("The unchanged Prime set =",primes,'\n')


### CALCULATE DIFFERENCE OF SETS ###
setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}

difference = setA.difference(setB) #Returns al of the elements from the first set(setB) that are not in the 2nd set(setA)
difference1 = setB.difference(setA) #Returns al of the elements from the first set(setA) that are not in the 2nd set(setB)
symmetrical_diff = setA.symmetric_difference(setB) #returns all elements that don't appear in both sets
print("All of the elements in setA that aren't in setB =",difference)
print("All of the elements in setB that aren't in setA =",difference1)
print("All of the elements that don't appear in both setA and setB =",symmetrical_diff)
print("The unchanged setA =",setA)
print("The unchanged setB =",setB,'\n')

#Modifying sets

setC = {1,2,3,4,5,6,7,8,9}
setD = {1,2,3,10,11,12}
print("setc =",setC)
print("setD =",setD,'\n')

setC.update(setD) #Updates set w/ elements from other set
print("Updated setC =",setC)

#intersection update
setE = {1,2,3,4,5,6,7,8,9}
setF = {1,2,3,10,11,12}
print("setE =",setE)
print("setF =",setF)

setE.intersection_update(setF) # Only shows which elements are duplicates in the
print("The duplicate elements between setE and setF =",setE)

#difference update = removes elements from setG if found in setH
setG = {1,2,3,4,5,6,7,8,9}
setH = {1,2,3,10,11,12}
print("setG =",setG)
print("setH =",setH)

setG.difference_update(setH) # Shows which elements don't appear in the called set
print("The elements in setG that don't appear in setH =",setG)

#symmetrical difference update = removes duplicate elements between two sets, and returns the remaining elements in the initial set
setI = {1,2,3,4,5,6,7,8,9}
setJ = {1,2,3,10,11,12}
print("setI =",setI)
print("setJ =",setJ)

setI.difference_update(setJ) # Removes which elements don't appear in the called set, and prints only the remaining elements
print("The duplicate elements found in both setI and setJ =",setI)

### SUPERSET, SUBSET and DISJOINT METHODS ###
setK = {1,2,3,4,5,6}
setL = {1,2,3}
print("setK =",setK)
print("setL =",setL)

print("Is setK a superset of setL?",setK.issuperset(setL))
print("Is setK a subset of setL?",setK.issubset(setL))


#Disjoint = checks to see if there are no same elements
setM = {1,2,3,4,5,6,7,8,9}
setN = {1,2,3,10,11,12}
print("setM =",setM)
print("setN =",setN)

print("Is setM a disjoint of setN?",setM.issuperset(setN))
print("Is setN a subset of setL?",setM.issubset(setM))


#Copy
setO = {1,2,3,4,5,6,7,8,9}
setP = {1,2,3,10,11,12}
print("setO =",setO)
print("setP =",setP)

setO = setP #assigns two sets to the same set element data


print("Now setO =",setO)
print("Now setP =",setP)

print('\n')

setQ = {1,2,3,4,5,6,7,8,9}
setR = {1,2,3,10,11,12}
print("setQ =",setQ)
print("setR =",setR)

setQ = setR.copy() #correct way to copy sets w/o overwriting data
print("Now setQ =",setQ)
print("Now setR =",setR)

print('\n')

setS = {1,2,3,4,5,6,7,8,9}
setT = {1,2,3,10,11,12}
print("setS =",setS)
print("setT =",setT)

setT = setS.copy() #another way to copy sets w/o overwriting data
print("After adding setS elements to setS,Now setS =",setT)
print("Now setT =",setS)

setS.add(7) #add elements to a set
print("Adding elements...setS =",setS)


print('\n')

#FROZEN SET = immutable version of a normal set

a = frozenset([1,2,3,4]) #create an immutable set
print("The frozenset =",a, "and is a data type =",type(a))

try:
    a.add(2)
except AttributeError:
    print("You encountered an Attribute Error.")

try:
    a.remove(2)
except AttributeError:
     print("You encountered an AttributeError")

try:
    a.union(setS)
    print(a)
except AttributeError:
     print("You encountered an AttributeError")
