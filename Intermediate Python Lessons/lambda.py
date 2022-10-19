"""
Lambda = small one line anonymous function defined w/o a name.
[Format] lambda arguements: expression
*Nominally used when you need a simple function used only once in your code; or as an arguement to higher order functions. (functions that take in other functions as arguements)
"""

add10 = lambda x: x + 10 #1 line function
print("Lambda function =",add10(5))

def add10_func(x): #same function as lambda function above
    return x + 10
print("Normal function =",add10_func(5))


#Multi-arguement lambda functions
mult= lambda x,y: x*y
print("Two arguement lambda function =",mult(2,3))

print('\n')

#Using lambdas w/ higher order functions
points2D = [(1,2),(15,1),(5,-1),(10,4)]
points2D_sorted = sorted(points2D) #sorts on first index in each tuple
points2D_sorted_lambda = sorted(points2D, key=lambda x: x[1]) #sorts on 2nd index in each tuple; inserting lambda function as an input to a higher order function

print(points2D)
print("Default Sorted =",points2D_sorted) ##sorts x values from points2D
print("Lambda Sorted on 2nd Elements =",points2D_sorted_lambda) #sorts y values from points2D

print('')
#comparing functions
def sort_by_y(x): #orignal way to sort using default functions
    return x[1]
points2D_sorted_function = sorted(points2D, key=sort_by_y) #sorts on 2nd index in each tuple

print("Original Sorting Function on 2nd Elemennt =",points2D_sorted_function)
print("Lambda Sorted on 2nd Element =",points2D_sorted_lambda)

print('\n')

#sorting according to sums
points2D = [(1,2),(15,1),(5,-1),(10,4)]

points2D_sorted_sum_lambda = sorted(points2D, key=lambda x: x[0] + x[1]) #sorts the sum of each tuple; inserting lambda function as an input to a higher order function
print(points2D)
print("Sorted Sum Using Lambda =",points2D_sorted_sum_lambda)

print('\n')


### Map Functions transforms each element w/ a function
# map(func,seq)

a = [1,2,3,4,5]
b = map(lambda x: x*2,a) #multiplies each element w/ specified function
print(a)
print("Mapped Lambda Method =",list(b))

#using list comprehension
c = [x*2 for x in a] #non-lambda way to accomplish the same goal
print("Regular List Comprehension Method =",c)

print('\n')


###Filter Function returns all elements that validate to True; All filter functions must return True or False
# filter(func,seq)

#greater than 2
a1 = [1,2,3,4,5]
b = filter(lambda x: x>2,a1) #returns each element that validate as True for the specified function
print(a1)
print("Greater Than 2 Filter Method =",list(b))

#all values that are even
a1 = [1,2,3,4,5]
b = filter(lambda x: x%2==0,a1) #eturns each element that validate as True for the specified function
print("All Even Elements =",list(b))

#alternate list comprehension method
c = [element for element in a1 if element % 2==0]
print("Using List Comprehension, All Even Elements =",c)

print('\n')


#Reduce Function repeatedly applies the function to the elements and returns a single value
# reduce(func,seq)
from functools import reduce

a2 = [1,2,3,4]

product_a = reduce(lambda x,y: x*y,a2) #multiplies each index by its adjacent index to reach a single value
print("Reduce Lambda, Product =",product_a) #no need to use a list to see value