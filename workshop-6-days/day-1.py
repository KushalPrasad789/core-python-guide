# =============================================================
# DAY 1 OF PYTHON PROGRAMMING WORKSHOP
# =============================================================

# This is  a comment
print("Hello World")

#pip - Python package manager

'''Doc string''' # This is a doc string

# Variables
a = 'hello'
a = 71
b = 20

# Operators

# Arithmetic operators
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
print("Floor Division:", a // b)

# Assignment operators
c = a + b
print("c = a + b:", c)

c += a
print("c += a:", c)

c -= a
print("c -= a:", c)

c *= a
print("c *= a:", c)

c /= a
print("c /= a:", c)

c %= a
print("c %= a:", c)

c **= a
print("c **= a:", c)

c //= a
print("c //= a:", c)


# Type operator
print("Type of a:", type(a))

a = 'text'
print("Type of a:", type(a))

# Type casting
print(str(a))
print(int(a))
print(float(a))
# Note that alpha numeric values can't be converted to int

# Taking user input
a = input("Enter a number: ")
b = input("Enter another number: ")
print("Addition:", a + b) # Results in concatenation because the input function returns a string

# Conversion of input dat to int
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
print("Addition:", a + b) # Results in addition because the input function returns an integer

# Comparision operators
a = 5
b = 7
print("Equal to:", a == b)
print("Not equal to:", a != b)
print("Greater than:", a > b)
print("Less than:", a < b)
print("Greater than or equal to:", a >= b)
print("Less than or equal to:", a <= b)


# Conditional Statements

# If statement
a = 5
b = 7
if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else:
    print("a is equal to b")
    
    
# Strings in C

# String to write a string
string = 'string'
string = "string"
# Both are correct but you can use double quotes if you want to use single quotes in the string
string = "I'm a string" # This is correct
string = 'I\'m a string' # This is also correct
# A backslash is used to escape the character that follows it

# String indexing
string = 'Hello World'
print(string[0]) # H
print(string[1]) # e
print(string[-1]) # d
print(string[-2]) # l

# String slicing
print(string[0:5]) # Hello
print(string[6:]) # World
print(string[:5]) # Hello
print(string[:]) # Hello World
# String slicing with steps
print(string[::2]) # HloWrd
print(string[::-1]) # dlroW olleH
# -1 is also used to reverse a string

# Length of a string
print(len(string)) # 11

# String methods
string = 'Hello World'
print(string.upper()) # HELLO WORLD
print(string.lower()) # hello world
print(string.capitalize()) # Hello world
print(string.title()) # Hello World
print(string.swapcase()) # hELLO wORLD
print(string.count('o')) # 2
print(string.find('o')) # 4
print(string.rfind('o')) # 7
print(string.index('o')) # 4
print(string.rindex('o')) # 7
print(string.startswith('Hello')) # True
print(string.endswith('World')) # True
print(string.replace('World', 'Everyone')) # Hello Everyone
print(string.split()) # ['Hello', 'World']
print(string.split('o')) # ['Hell', ' W', 'rld']
print(string.join(['Hello', 'World'])) # HelloWorld
print(string.strip()) # 'Hello World'
print(string.lstrip('H')) # 'ello World'
print(string.rstrip('d')) # 'Hello Worl'
# Strings can also be used instead of characters in the above methods

# Escape Sequences
print('Hello\nWorld') # Hello
                      # World
print('Hello\tWorld') # Hello    World
print('Hello\\World') # Hello\World
print('Hello\'World') # Hello'World
print('Hello\"World') # Hello"World
print('Hello\bWorld') # HellWorld
print('Hello\rWorld') # World
                      # This is because \r moves the cursor to the beginning of the line
print('Hello\fWorld') # Hello
                        #     World
                        # This is because \f moves the cursor to the next line

# print() function
print('Hello', 'World') # Hello World
print('Hello', 'World', sep=' ') # Hello World
print('Hello', 'World', sep='') # HelloWorld
print('Hello', 'World', sep='\n') # Hello
                                   # World
# These two lines combinely print Hello World
print('Hello', end=' ') # Hello
print('World') # World

# Printing different types of data
a = 5
b = 7
print('a is', a, 'and b is', b) # a is 5 and b is 7
# Formatting strings
print('a is {} and b is {}'.format(a, b)) # a is 5 and b is 7
# fstrings
print(f'a is {a} and b is {b}') # a is 5 and b is 7

# A program to display a user entered name followed by Good Afternoon using the fstring
name = input("Enter your name: ")
print(f'Good Afternoon, {name}')

# List
# A list is a collection of items in a particular order
# Lists are mutable
# Lists are defined using square brackets
# Lists can contain any type of data
# Lists can contain duplicate data
list = [1, 2, 3, 4, 5] # A list of integers
list = ['a', 'b', 'c', 'd', 'e'] # A list of characters
list = [1, 'a', 2, 'b', 3, 'c'] # A list of integers and characters
list = [1, 1, 2, 2, 3, 3] # A list of duplicate integers
list = [] # An empty list

# Accessing elements in a list
list = [1, 2, 3, 4, 5]
print(list[0]) # 1
print(list[1]) # 2
print(list[-1]) # 5
print(list[-2]) # 4

# Slicing a list
# Slicing a list returns a new list and it is similar to the slicing of a string
print(list[0:3]) # [1, 2, 3]
print(list[2:]) # [3, 4, 5]
print(list[:3]) # [1, 2, 3]
print(list[:]) # [1, 2, 3, 4, 5]
print(list[::2]) # [1, 3, 5]
print(list[::-1]) # [5, 4, 3, 2, 1]
# -1 is also used to reverse a list

# Length of a list
print(len(list)) # 5

# Modifying elements in a list
list = [1, 2, 3, 4, 5]
list[0] = 6
print(list) # [6, 2, 3, 4, 5]

# Sorting a list
# Only the numbers can be sorted
# The sort() method sorts the list in ascending order in same list i.e it modifies the original list
list = [5, 2, 3, 4, 1]
list.sort() # Ascending order
print(list) # [1, 2, 3, 4, 5]

# Copying a list
l1 = [1, 2, 3, 4, 5]
l2 = l1 # This is not copying the list but it is creating a reference to the list
# If we modify l2, l1 will also be modified
l2[0] = 6
print(l1) # [6, 2, 3, 4, 5]
print(l1 is l2) # True 
# To copy a list, we use the copy() method
# The copy() method copies the list to another list
l1 = [1, 2, 3, 4, 5]
l2 = l1.copy()
l2[0] = 6
print(l1) # [1, 2, 3, 4, 5]
print(l1 is l2) # False

# Reversing a list  
# Does not return a new list but modifies the original list
list = [1, 2, 3, 4, 5]
list.reverse()
print(list) # [5, 4, 3, 2, 1]

# Appending elements to a list
list = [1, 2, 3, 4, 5]
list.append(6)
print(list) # [1, 2, 3, 4, 5, 6]

# Inserting elements to a list
list = [1, 2, 3, 4, 5]
list.insert(0, 6)
print(list) # [6, 1, 2, 3, 4, 5]
# This will insert a new element at the specified index and shift the rest of the elements to the right
# To replace an element at a particular index, we can use the assignment operator
list[0] = 7
print(list) # [7, 1, 2, 3, 4, 5]
# .replace() method can also be used to replace an element at a particular index
list.replace(0, 8)
print(list) # [8, 1, 2, 3, 4, 5]

# Removing  the elements from a list
list = [1, 2, 3, 4, 5]
popped_item = list.pop() # Returns the last element and removes it from the list
print(popped_item) # 5
# For removing an element at a particular index
popped_item = list.pop(0) # Returns the element at the specified index and removes it from the list
print(popped_item) # 1

# Removing an element by value
# This will remove the first occurence of the element
# If the element is not present in the list, it will throw an error
# Returns None
list = [1, 2, 3, 4, 5]
list.remove(3)
print(list) # [1, 2, 4, 5]

# Note that the pop() takes the index but the remove() takes the value


# Tuples
# immutable
# defined using parentheses
# can contain any type of data similar to lists
# can contain duplicate data similar to lists
tuple = (1, 2, 3, 4, 5) # A tuple of integers
tuple = ('a', 'b', 'c', 'd', 'e') # A tuple of characters
tuple = (1, 'a', 2, 'b', 3, 'c') # A tuple of integers and characters
tuple = (1, 1, 2, 2, 3, 3) # A tuple of duplicate integers
tuple = () # An empty tuple
print(type(tuple)) # <class 'tuple'>
print(tuple) # ()

# No assignment and modifications
# tuple[0] = 6 # This will throw an error

# Indexing and slicing is similar to lists
tuple = (1, 2, 3, 4, 5)
print(tuple[0]) # 1
# .index() method can be used to find the index of an element
print(tuple.index(1)) # 0

# len() function can be used to find the length of a tuple
print(len(tuple)) # 0

# count() method can be used to count the number of occurences of an element
print(tuple.count(1)) # 1


# Program to input 3 fruits name and append all the fruits to a list
fruits = []
fruits.append(input("Enter a fruit name: "))
fruits.append(input("Enter a fruit name: "))
fruits.append(input("Enter a fruit name: "))
print(fruits)

# Program to input 3 marks and append all the marks to a list. Print the marks after sorting
marks = []
marks.append(int(input("Enter a mark: ")))
marks.append(int(input("Enter a mark: ")))
marks.append(int(input("Enter a mark: ")))
marks.sort() # Ascending order sorting
print(marks)


# Dictionaries
# A dictionary is a collection of key-value pairs
# Dictionaries are mutable
# Dictionaries are defined using curly braces
# Dictionaries can contain any type of data
# Dictionaries can contain duplicate data
# Dictionaries are unordered
# Dictionaries are indexed by keys
# They are unordered and hence cannot be sliced
dict = {
    'name' : 'Kushal Prasad Joshi',
    'age' : 20,
    'roll' : 230345
}
print(type(dict)) # <class 'dict'>
print(dict) # {'name': 'Kushal Prasad Joshi', 'age': 20, 'roll': 230345}

# Accessing elements in a dictionary
# Elements are accessed using keys
print(dict['name']) # Kushal Prasad Joshi
print(dict['age']) # 20
# If the key is not present in the dictionary, it will throw an error

# We can store the lists and tuples in a dictionary
dict = {
    'name' : 'Kushal Prasad Joshi',
    'age' : 20,
    'roll' : 230345,
    'marks' : [90, 80, 70],
    'subjects' : ('Maths', 'Science', 'English')
}
print(dict['marks']) # [90, 80, 70]
print(dict['subjects']) # ('Maths', 'Science', 'English')
print(dict)

# There can be another dictionary inside a dictionary
dict = {
    'name' : 'Kushal Prasad Joshi',
    'age' : 20,
    'roll' : 230345,
    'marks' : [90, 80, 70],
    'subjects' : ('Maths', 'Science', 'English'),
    'address' : {
        'city' : 'Kathmandu',
        'state' : 'Bagmati',
        'country' : 'Nepal'
    }
}
print(dict['address']) # {'city': 'Kathmandu', 'state': 'Bagmati', 'country': 'Nepal'}
print(dict['address']['city']) # Kathmandu

# .keys(), .values(), .items() methods
dict = {
    'name' : 'Kushal Prasad Joshi',
    'age' : 20,
    'roll' : 230345,
}
print(dict.keys()) # dict_keys(['name', 'age', 'roll', 'marks', 'subjects', 'address'])
print(dict.values()) # dict_values(['Kushal Prasad Joshi', 20, 230345, [90, 80, 70], ('Maths', 'Science', 'English'), {'city': 'Kathmandu', 'state': 'Bagmati', 'country': 'Nepal'}])
print(dict.items()) # dict_items([('name', 'Kushal Prasad Joshi'), ('age', 20), ('roll', 230345), ('marks', [90, 80, 70]), ('subjects', ('Maths', 'Science', 'English')), ('address', {'city': 'Kathmandu', 'state': 'Bagmati', 'country': 'Nepal'})])

# Adding elements to a dictionary
dict = {
    'name' : 'Kushal Prasad Joshi',
    'age' : 20,
    'roll' : 230345,
}
dict['marks'] = [90, 80, 70]
dict['subjects'] = ('Maths', 'Science', 'English')

# Removing elements from a dictionary
dict = {
    'name' : 'Kushal Prasad Joshi',
    'age' : 20,
    'roll' : 230345,
}
dict.pop('age')

# Clearing a dictionary
dict = {
    'name' : 'Kushal Prasad Joshi',
    'age' : 20,
    'roll' : 230345,
}
dict.clear()


# Sets
# A set is a collection of unique elements
# Sets are unordered
# Sets are mutable
# Sets are defined using curly braces
# Sets can contain any type of data
# Sets cannot contain duplicate data
set = {1, 2, 3, 4, 5} # A set of integers
set = {'a', 'b', 'c', 'd', 'e'} # A set of characters
set = {1, 'a', 2, 'b', 3, 'c'} # A set of integers and characters
set = set() # An empty set
print(type(set)) # <class 'set'>
print(set) # set()

# Accessing elements in a set
# Elements cannot be accessed using indexes because sets are unordered
# Elements can be popped using the pop() method
set = {1, 2, 3, 4, 5}
print(set.pop()) # 1
