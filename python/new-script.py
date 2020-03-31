#!/bin/python3

# Importing Modules

import sys # Must be specified to run any sys commands - sys deals with system functions and parameters
from datetime import datetime as dt# Importing a specific part of datetime with an alias

print(sys.version) # prints "3.7.7 (default, Mar 10 2020, 13:18:53)"
print(dt.now()) # 2020-03-29 14:50:07.291150


my_name = "Jackson"
print(my_name[0]) # Prints first initial
print(my_name[-1]) # Prints last letter of name
print(my_name[4]) # Prints fifth letter of name

sentence = 'This is a sentence.'
print(len(sentence)) # 19
print(sentence[:4])  # Prints out 'This'
print(sentence.split()) # Prints out all words separated by a space - ['This', 'is', 'a', 'sentence.']

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split) # Joins words togethor removing the delimeter of ''
print(sentence_join) # This is a sentence
print(sentence_split) # ['This', 'is', 'a', 'sentence.']

quote = "He said, 'give me all your money'" # Would not accept double quotations inside the variable
print(quote) # He said, 'give me all your money'

quote = "He said, \"give me all your money\"" # Ignores anything between \ and treats as a string - Character escape
print(quote)

too_much_space = "                              hello                 "
print(too_much_space.strip()) # removes all the extra space by stripping it

print("A" in "Apple") # Returns True because Capital A is in Apple

print("a" in "Apple") # Returns False because lowercase a is NOT in Apple

letter = "A" # looking for this letter
word = "Apple" # looking in this word
print(letter.lower() in word.lower()) # Returns True - Improved - No need to worry about case sensitivity

movie = "The Hangover"
print("My favorite movie is {}".format(movie)) # My favorite movie is The Hangover


age = 25
print("I am {} years old".format(age)) # I am 25 years old - Adds a placeholder and updates with whatever the variable is set at. Better than doing regular concatenation

def nl():
	print("\n")
	
nl()

# Dictionaries - key/value pairs {}

drinks = {"White Russian": 7, "Old Fashion": 10, "Lemon Drop": 8} # Drinks is a key, Price is a value
print(drinks)

#drink_split = drink.split()
#drink_join = ' '.join(drink_split) # You cannot join a dict
#print(drink_join)

nl()
employees = {"SOC": ["Jackson", "Matthew", "Kenneth", "Hayley", "Savannah", "Aaron", "Brian"], "DCO": ["Mark", "Dan", "Brian. D"], "OCO": ["Martin"]}
print(employees)

employees['Legal'] = ["Mr. Frond"] # Adds new key value pair for Legal

print(employees)

employees.update({"Sales": ["Brice"]}) # Appends Sales to the employee dictionary

print(employees)

drinks['White Russian'] = 8 # White russian key now has a value of 8
print(drinks)

print(drinks.get("White Russian")) # Gets White Russian from the dictionary and returns its value

print(employees.get("SOC")) # Prints ['Jackson', 'Matthew', 'Kenneth', 'Hayley', 'Savannah', 'Aaron', 'Brian']



























sys.exit() # Exits python cleanly - Must have for python scripts
