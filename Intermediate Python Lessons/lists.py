"""
Lists = data type that is ordered, mutable, and allows duplicate elements.
"""

mylist = ["banana","cherry","apple"]
print(mylist)

mylist2 = list() #creates an empy new list
print(mylist2)

mylist3 = [5,True, "aaple","apple"]
print(mylist3)

item = mylist[0] #first item is index of 0
print(item)

last_item = mylist[-1] # -1 is the last item in the list
print(last_item)

for value in mylist: #print every value in list on a new line
    print(value)

if "banana" in mylist:
    print('Yes your requested value is in the defined list.')
else:
    print('No your requested value is not in the defined list.')

print(len(mylist)) #check to see how many elements exist in your list)

mylist.append('waffles') #add items to the end of the list
print(mylist)

mylist.insert(1,'pancakes') #add an item to a specific location
print(mylist)

popped_off_mylist = mylist.pop() #remove only the last item from the list; also stores what that popped off value is
print('The modified popped off list = ',mylist, 'The popped off element = ',popped_off_mylist,'\n')

mylist.remove('cherry') #remove a specific element
print('After removing an element, mylist = ',mylist)

mylist3.clear() #remove all elements from the list
print('The cleared mylist3 = ', mylist3)

reversed_mylist = mylist.reverse() #reverse the list
print('The reversed mylist = ',mylist,'\n')

mylist4 = [2,66,24,9,-84]
mylist5 = ['junk food','healthy food','tequila']
mylist4.sort() #sorts the list and saves it; this also sorts strings by alphabetical order
new_sorted_mylist = sorted(mylist) #create a NEW SORTED list from the original list
mylist5.sort() #sorts a string list AND this modifies the original list
print('mylist4 =',mylist4)
print('The newly created sorted mylist = ',new_sorted_mylist)
print('mylist5 = ',mylist5,'\n')

mylist6 = [0] * 5 #create a new list w/ math
print('math created new list', mylist6)

concatenated_list = mylist6 + mylist5 #concatenate 2 lists
print('Concatenated list w/ mylist5 & mylist6 = ',concatenated_list)

#slicing: accessing subparts of your list
mylist7 = [1,2,3,4,5,6,7,8]
a = mylist7[1:5]
print(a)
b = mylist7[0:8:3] #searches from the begining to the end, by stepping by threee (skipping 3 elements over until compolete)
c = mylist7[::3] #same as above; searches from the begining to the end, by stepping by threee (skipping 3 elements over until compolete)
print('Stepping list = ', b,c)

#making copies of lists
list_original = ['book','ice','car']
list_copy = list_original #this copy method links two list to reference the same data/memory
list_copy.append('lemon')
print('Linked Data copied list = ',list_copy, ' and original list = ', list_original)

list_original2 = ['oh yeah', 'time to eat some slime!','Its ALLLLL THAAAAT']
list_copy2 = list_original2.copy() #this correctly copies the data to a NEW variable w/o linking to original data
#list_copy2 = list(list_original) #alternate way to accomplish what's above
#list_copy2 = list_original[:]  #alternate way to accoplist what's above using slicing
list_copy2.append('lemon')
print('Unlinked Data copied list = ',list_copy2, ' and original list = ', list_original2,'\n')

#list comprehension
a = [1,2,3,4,5,6]
b = [i*i for i in a]
print('original list = ', *a)
print('The squared of the above list = ',b)