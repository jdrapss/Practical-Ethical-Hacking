#!/bin/python3

#Variables and Methods

quote = "All is fair in love and war." # Variable
print(quote.upper()) # uses the .upper() method to force uppercase

print(quote.lower()) # uses the .lower() method to force lowercase

print(quote.title()) # uses the .title() method to force a Title (Capitalizes the first letter of each word in a string)


#print the length of quote
print(len(quote)) #28

name = "Jackson" # string
age = 25 # int
gpa = 3.42 # float

print(int(age))
print(int(25.6))

# print("My name is " + name + " and I am " + age + " years old.") # can only concatenate str (not "int") to str

print("My name is " + name + " and I am " + str(age) + " years old.") # str(variable) allows you to convert numbers into a string to be able to print out)

age +=1 # Adding 1 to age
print(age)

birthday = 1
age += birthday
print(age) # Note the age variable is now stored with 26 due to the age +=1 operator

print('\n')
#Functions
print("Here is an example function:")

def who_am_i(): # this is a function
	name = "Jackson" # This variable is only stored inside this function
	age = 25 # This variable is only stored inside this function
	print("My name is " + name + " and I am " + str(age) + " years old.") 
	
who_am_i()

# adding parameters

def add_one_hundred(num): # num is a generic function for a number
	print(num + 100)
	
add_one_hundred(50) # prints 150

# multiple parameters
def add(x,y):
	print(x + y)
	
add(7,7)
# Testing with strings
def fav_songs(x,y):
	print(x + y)
	x = 'Sledgehammer'
	y = 'Fade Away'
	print('My favorite songs are ' + x + ' and ' + y)
	
fav_songs('Sledgehammer', 'Fade Away') # prints 'My favorite songs are Sledgehammer and Fade away'

# Return functions and output
def multiply(x,y):
	return x * y # does not print, only returns the value
	
multiply(7,7) # no print function. Only returns

print(multiply(7,7)) # 49

# 
# My version of a square root function
def square_root_j(x):
	return x ** .5

print(square_root_j(16)) # Prints float value of 4.0

# Cleaned up version of a square root function
def square_root_h(x):
	print(x ** .5)
	
square_root_h(16) # prints float value of 4.0

# Return functions are not always necessary. Look for ways to clean the code up

# Define a function for printing ('\n')
def nl():
	print('\n')
	
nl()

print("Hello, World!")

nl()

def covid_cases(x,y,z):
	x = 'New York'
	y = 'California'
	z = 'Texas'
	print(x + " has the highest number of reported cases of COVID-19." + " The second highest number of cases is in " + y + ". " + "The third highest amount of reported cases is in " + z + ".")
	
covid_cases('New York','California','Texas')
 
# Boolean Expressions (True or False)

print("Boolean expressions:")

bool1 = True # True
bool2 = 3*3 == 9 # True
bool3 = False # False
bool4 = 3*3 != 9 # False

print(bool1,bool2,bool3,bool4) # True True False False
print(type(bool1)) # <class 'bool'>

# Relational and Boolean Operators
nl()
greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7

print(greater_than, less_than, greater_than_equal_to, less_than_equal_to) # True True True True
nl()
print('Using and/or with boolean operators:')
test_and = (7 > 5) and (5 < 7) # True
test_and2 = (7 > 5) and (5 < 7) # Entire statement is now false because of and
test_or = (7 > 5) or (5 < 7) # True
test_or2 = (7 > 5) or (5 > 7) # True

# With 'or' operators, only one statement has to be true to make the boolean result = True
# With 'and' operators, both statements must be true to make the boolean result = True

print(test_and, test_and2, test_or, test_or2)

test_not = not True #False

# Using Boolean for Flow Control

grade = 73
if grade >= 69:
	print("You passed!")
	
else:
	print("You failed")

print(grade)	


# Testing calling functions

def guess_what():
	guess1 = 'Chicken'
	guess2 = 'Butt'
	print("Guess what? " + guess1 + " " + guess2 + ".")
	
guess_what()

nl()
#Conditional Statements

def drink(money):
	if money >= 2:
		return "You've got yourself a drink!"
	else:
		return "NO drink for you!"

print(drink(1))
print(drink(3))
nl()

def alcohol(age,money):
	if (age >= 21) and (money >= 5):
		return "You can drink!"
	#elif (age <= 21) or (money >= 5):
		#return "You cannot drink"
	elif (age >= 21) and (money < 5):
		return "I get you're of age, but come back when you have more money"
	elif (age < 21) and (money >= 5):
		return "I dont care how much money you have. Come back when you are 21!"
	else: 
		return "You cannot drink!"
		
print(alcohol(22,6)) # You can drink!
print(alcohol(20,3)) # You cannot drink!
print(alcohol(22,4)) # I get you're of age, but come back when you have more money
print(alcohol(20,6)) # I dont care how much money you have. Come back when you are 21!

nl()

#Lists - Have brackets []

movies = ["Law Abiding Citizen", "Pulp Fiction", "Kill Bill Vol.1", "Natural Born Killers"]
print(movies[1]) # The first item in a list is 0 -> this returns the second item
print(movies[0]) # Law Abiding Citizen
print(movies[1:3]) # Returns in brackets and quotes up until Kill Bill Vol.1
print(movies[1:4]) # ['Pulp Fiction', 'Kill Bill Vol.1', 'Natural Born Killers']
print(movies[0:]) # Returns 0 and anything after it in the list
print(movies[:1]) # Grabs everything before 1 -> Law Abiding Citizen
print(movies[-1]) # Grabs the last item -> Natural Born Killers

print(len(movies)) # Counts the amount of items in the list -> 4

movies.append("Jaws")
print(movies) # Jaws adds itself at the end of the list

movies.pop() # deletes the very last item in the list
print(movies)

movies.pop(0) # Removes the first item in a list
print(movies)

nl()
# Tuples - Do not change, ()

grades = ("a", "b", "c", "d", "f")
#Grades.pop(0) # Cannot remove from a tuple
print(grades)
print(grades[1]) # Prints b


nl()
# Looping
# For Loops - start to finish of an iterate
vegetables = ["Cucumber", "Spinach", "cabbage"]
for x in vegetables:
	print(x) # Iterates through the entire list
	
# While Loops - Executes as long as true:

i = 1

while i < 10:
	print(i)
	i += 1 # Prints constantly until it reaches 10, then must stop
	

	

	
