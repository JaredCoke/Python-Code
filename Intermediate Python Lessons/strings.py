"""
Strings: An ordered and immutable data type used for text representation.
"""

my_string = "Hello World" #create a string
print(my_string)
my_string2 = 'Hello World' #another way to create a string
print(my_string2)
my_stringa = "I'm a programmer" #create a string w/o issue using '
print(my_stringa)
my_string2a = 'I\'m a programmer' #creates a string handlng the issue using '
print(my_string2a)

print('\n')

my_string3 = """Hello
WOrld""" #creates a string that spans multiple lines
print(my_string3)

my_string3 = """Hello \
WOrld""" #creats a one line sting
print(my_string3)

print('\n')

### ACCESSING CHARACTERS
my_string4 = "Hello World"
char = my_string4[1] #returns 2nd element/character
print(char)
char = my_string4[-1] #returns last element/character
print(char)

try:
    my_string4[0] ='h' #Attempt to change an indexed character
    print(my_string4)
except TypeError:
    print('Ha. Strings are immutable, silly. You can\'t change these values.')

print('\n')

### SLICING ###
my_string5 = "Hello World"
substring = my_string[1:5] #returns index 1 - 4, since the last specified index is excluded
print('substring =',substring)
substring2 = my_string[1:] #returns index 1 - everything else
print('substring2 =',substring2)
substring3 = my_string[:5] #returns index everything until index 4, since last specified index is excluded
print('substring3 =',substring3)

substring4 = my_string[::1] #returns everything
print('substring4 =',substring4)
substring5 = my_string[::3] #returns the 3rd character
print('substring5 =',substring5)

substring6 = my_string[::-1] #reverses the entire string
print('substring6 =',substring6)
substring7 = my_string[::-3] #reverses the entire string and returns every 3rd character
print('substring7 =',substring7)

print('\n')

### Concatenating Two or More Strings ###
greeting = 'Hello'
name = "Jamal"
sentence = greeting + " " + name #adds two strings together w/ a space
print(sentence)


#LOOPING
for character in greeting: # loops through every character/element inside greeting
    print(character)

### Conditionals
#commenting out older way
element = 'ello'
if element in greeting:
    #print('Yes! \'ello\' exists in greeting.')
    print(f'Yes! {element} exists in greeting.')
else:
    #print("Nope. 'ello' does not exists in greeting.")
    print(f'Nope. {element} does not exists in greeting.')
print('\n')

#Manipulating Strings Stored in New Strings
my_string6 = '      Hello World     '
print('The tabbed out string=',my_string6)
my_string6 = my_string6.strip() #This method removes excessive/tab white space; regular spaces remain; this re-assigns the new string to a value
print('The stripped out tabs string =',my_string6)

print('\n')

my_string7 = 'Hello World'
print('my_string7=',my_string7)
print('The upper case my_string7 =',my_string7.upper()) #returns the string in all caps; doesn't alter the original string variable tho
print('The lower case my_string7 =',my_string7.lower()) #returns the string in all lower cases; doesn't alter the original string variable tho
print('The original string is still unaltered too! my_string7 =',my_string7)

print('Does my_string7 begin w/ \'Hello\'?',my_string7.startswith('Hello')) #Returns True/False if conditional passes
print('Does my_string7 end w/ \'d\'?',my_string7.endswith('d')) #Returns True/False if conditional passes

print('Where is character \'o\' located in my_string7? Index =',my_string7.find('o')) #Returns the 1st index where a requested character is found
print('Where is character \'lo\' located in my_string7? Index =',my_string7.find('lo')) #Returns the 1st index where a requested string is found
print('Where is character \'wafffles\' located in my_string7? Index =',my_string7.find('waffles')) #-1 means the string/character doesn't exist in string
print('How many times does \'o\' appear in my_string7? Times =',my_string7.count('o')) #Returns total times character/string appears

print('The replaced string =',my_string7.replace('World', 'Tequila')) #Replaces a word
print('The original string is still unaltered too! my_string7 =',my_string7)
print('The failed replaced string =',my_string7.replace('does not exist', 'Tequila')) #Fails at replacing; returns original string

print('\n')

### LIST and STRINGS
my_string8 = 'how are you doing'
my_list1 = list(my_string8) #puts each string character in a list
print('Every character stored as a list =',my_list1)
my_list2 = my_string8.split() #puts each string word in a list; default deliminator = " " | space
print('Using default split, Every word stored as a list =',my_list2)
my_list3 = my_string8.split(" ") #another way to put each string word in a list
print('Using split with \" \", Every word stored as a list =',my_list3)

my_string8a = 'how,are,you,doing'
my_list4 = my_string8.split(",") #put each string separated by a comma in a list - stores it as one element if none are found
my_list4a = my_string8a.split(",") #put each string separated by a comma in a list
print('Every commafied word stored as a list =',my_list4)
print('Every commafied word stored as a list =',my_list4a)

#revert list back to a string
new_string = ''.join(my_list4) #reverts one list element with spaces back to string
new_stringa = ''.join(my_list4a) #reverts list full of strings w/ no spaces to a one worded string
new_stringb = ' '.join(my_list4a) #reverts list full of strings w/ spaces between each list element
new_stringc = ','.join(my_list4a) #reverts list full of strings w/ commas between each list element
print('Reverting every commafied word stored as a list => string =',new_string)
print('Reverting every commafied word stored as a list => string =',new_stringa) #notice the spacing gets messed up here
print('Reverting every commafied word stored as a list => string =',new_stringb) #nicely formatted
print('Reverting every commafied word stored as a list => string =',new_stringc) #places commas

print('\n')


my_list5 = ['a'] * 6
print('my_list5 =',my_list5)

#BAD PYTHON CODE !!! IT's very memory expensive since it creates a new string multiple times
my_string9 = ''
for element in my_list5:
    my_string9 += element #creates a new string and then re-assigns it back to original string w/ new elements
print('Bad Way: List converted to a string =',my_string9)

#BETTER PYTHON CODE  =) !!!
my_string9 = ''.join(my_list5) #creates a new string and then re-assigns it back to original string w/ new elements
print('Better Way: List converted to a string =',my_string9)

#let's compare the bad vs better python code mentioned above
from timeit import default_timer as timer

my_list5 = ['a'] * 1000000 # increasing elements to 1mil for sake of comparision purposes

start = timer()
my_string9 = ''
for element in my_list5:
    my_string9 += element #creates a new string and then re-assigns it back to original string w/ new elements
stop = timer()
print(stop-start)

start = timer()
my_string9 = ''.join(my_list5) #creates a new string and then re-assigns it back to original string w/ new elements
stop = timer()
print(stop-start) #prints total time; this is the faster code

print('\n')

### FORMATTING STRINGS: Inserting variables inside quotes
#options: %, .format(), or f-Strings

#Oldest formating style
var = "Jacques"
my_string10 = "the variable is %s" %var #inserts a string only regardless of original data type
print(my_string10)

var_a = 92.45
my_string10a = "the variable is %d" %var_a #inserts a decimal/integer number
print(my_string10a)

var_b = 92.45
my_string10a1 = "the variable is %f" %var_b #inserts a floating number
print(my_string10a1)
my_string10a2 = "the variable is %.2f" %var_b #inserts a 2-decimal digit floating number
print(my_string10a2)

print('\n')

#Newer formating style
var2 = 3.1234567
my_string10b = 'the variable is {}'.format(var2) #inserts a variable
print(my_string10b)
my_string10b1 = 'the variable is {:.2f}'.format(var2) #inserts a float variable w/ only 2-decimal places
print(my_string10b1)
my_string10b2 = 'the variable is {:.2f} and {}'.format(var2,var) #inserts multiple varaibles
print(my_string10b2)

#Modern | Newest formatting style
var3 = 55.92
my_string10c = f'the variables are {var3} and {var}' #best way to insert variables; is fastest way; only works on python 3.6+
print(my_string10c)
my_string10c = f'the modified variables are {var3*2} and {var*4}' #best way to insert variables; is fastest way; only works on python 3.6+
print(my_string10c)