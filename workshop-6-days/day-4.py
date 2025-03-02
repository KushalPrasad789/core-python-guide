# =============================================================
# DAY 4 OF PYTHON PROGRAMMING WORKSHOP
# =============================================================

# Try except block is used to handle exceptions in Python.
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print('Result:', result)

except ValueError:
    print('Invalid input. Please enter numbers only.')

finally:
    print('This block will always execute.')
    # The finally block is used to execute the code whether the try block raises an exception or not.

print("This will not run if an exception occurs.")


# Else with Try Except
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print('Result:', result)

except ValueError:
    print('Invalid input. Please enter numbers only.')

else:
    print('This block will execute only if no exception occurs.')


# Raise an exception
try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError('Age cannot be negative.')
    print('Your age is:', age)

except ValueError as e:
    print(e)

# Another example of rase an exception
try:
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    if num2 == num3:
        raise ZeroDivisionError('Number 2 and 3 cannot be equal.')
    result = num1 / (num2 - num3)
    print('Result:', result)
except ZeroDivisionError as e:
    print(e)


# WAP to store rollnos in a list. If the roll number are same then raise an exception ValueError
rollnos = []
while True:
    try:
        rollno = int(input('Enter roll number: '))
        if rollno in rollnos:
            raise ValueError('Roll number already exists.')
        rollnos.append(rollno)
    except ValueError as e:
        print(e)

# Raise an exception in different function and handle it in main function
def divide(x, y):
    if y == 0:
        raise ZeroDivisionError('Cannot divide by 0')
    return x / y

try:
    result = divide(10, 0)
    print('Result:', result)
except ZeroDivisionError as e:
    print(e)

# Raise an exception in different function and handle it in main function (another method)
def divide(x,y):
    try:
        result = x / y
    except ZeroDivisionError:
        print('Cannot divide by 0')
        raise
    return result

try:
    result = divide(10, 0)
    print('Result:', result)
except ZeroDivisionError as e:
    print(e)


# Input 3 sides of traingle and check if the traingle is valid or not. Raise error inside function and handle it in main function
def is_valid_triangle(a, b, c):
    if a + b <= c or b + c <= a or c + a <= b:
        raise ValueError('Invalid triangle sides.')
    
    return True

try:
    a = int(input('Enter side 1: '))
    b = int(input('Enter side 2: '))
    c = int(input('Enter side 3: '))
    if is_valid_triangle(a, b, c):
        print('Valid triangle sides.')
    
except ValueError as e:
    print(e)


# Recursion
def factorual(n):
    if n == 0:
        return 1
    return n * factorual(n - 1)

result = factorual(5)
print('Factorial:', result)

# Sum of natural numbers from 1 to 10 using recursion
def sum_natural(n):
    if n == 0:
        return 0
    return n + sum_natural(n - 1)

result = sum_natural(10)
print('Sum of natural numbers:', result)

# Fibonacci series using recursion
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(10):
    print(fibonacci(i), end=' ')


# Function overloading
def add(x, y):
    return x + y

def add(x, y, z):
    return x + y + z

# This will give error as function overloading is not supported in Python
# print(add(10, 20))
print(add(10, 20, 30))
# The first defination is overwritten by the second defination. So, the first defination is not available.

# Lambda function
# Lambda function is an anonymous function in Python. It is defined using the lambda keyword.
# Lambda functions can have any number of arguments but only one expression.
# Syntax: lambda arguments: expression
add = lambda x, y: x + y
result = add(10, 20)
print('Result:', result)

# map() function
# The map() function is used to apply a function to all the elements in a list.
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print('Squares:', squares)

# filter() function
# The filter() function is used to filter the elements in a list based on a condition.
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print('Even numbers:', even_numbers)

# reduce() function
# The reduce() function is used to reduce the elements in a list to a single value.
from functools import reduce # Import reduce function from functools module as it is a library function

numbers = [1, 2, 3, 4, 5]
sum = reduce(lambda x, y: x + y, numbers)
print('Sum:', sum)


# File handling
# write to a file
file = open('example.txt', 'w') # Open a file in write mode
file.write('Hello, World!') # Write to the file
file.close() # Close the file

# read from a file
file = open('example.txt', 'r') # Open a file in read mode
content = file.read() # Read the content of the file
print('Content:', content)
file.close() # Close the file

# Another way to open a file
# The with statement is used to open a file and automatically close it after the block of code is executed.
# Wrie to a file
with open('example.txt', 'w') as file:
    file.write('This is a line in the file.')
    file.write('\nThis is another line in the file.')

# Read from a file
with open('example.txt', 'r') as file:
    content = file.read()
    print('Content:', content, end='') # end='' is used to remove the newline character at the end of the string

# Json file handling
import json # Import json module to

dict = {'name': 'John', 'age': 25, 'city': 'New York'} # Create a dictionary

with open('data.json', 'w') as file: # Open a file in write mode
    json.dump(dict, file) # Write the dictionary to the file

with open('data.json', 'r') as file: # Open a file in read mode
    data = json.load(file) # Load the data from the file
    print('Data:', data) # Print the data


# Type hinting
# Type hinting is used to specify the type of the arguments and return value of a function.
def add(x: int, y: int) -> int:
    return x + y

result = add(10, 20)
print('Result:', result)



# Crete a student management system using functions and file handling
import json

# 1. Add student function
def add_student():
    name = input('Enter student name: ')
    age = int(input('Enter student age: '))
    roll = int(input('Enter student roll number: '))
    marks = int(input('Enter student marks: '))
    return {'name': name, 'age': age, 'roll': roll, 'marks': marks}

# 2. Display student function
def display_student(student):
    print('Name:', student['name'])
    print('Age:', student['age'])
    print('Roll:', student['roll'])
    print('Marks:', student['marks'])

# 3. Search student function
def search_student(roll, students):
    for student in students:
        if student['roll'] == roll:
            return student
    return None

# 4. Update student function
def update_student(roll, students):
    student = search_student(roll, students)
    if student:
        student['name'] = input('Enter student name: ')
        student['age'] = int(input('Enter student age: '))
        student['roll'] = int(input('Enter student roll number: '))
        student['marks'] = int(input('Enter student marks: '))
    else:
        print('Student not found')

# 5. Save students to file
def save_students(students):
    with open('students.json', 'w') as file:
        json.dump(students, file)

# 6. Load students from file
def load_students():
    try:
        with open('students.json', 'r') as file:
            students = json.load(file)
    except FileNotFoundError:
        students = []
    return students

# 7. Exit program function
def exit_program():
    print('Exiting program')
    exit()

# Driver code
students = [] # Empty list for the students

while True:
    print('='*20)
    print('1. Add student')
    print('2. Display student')
    print('3. Search student')
    print('4. Update student')
    print('5. Save students')
    print('6. Load students')
    print('7. Exit')
    print('-'*20)

    choice = int(input('Enter your choice: '))

    match choice:
        case 1: # Add student
            students.append(add_student())

        case 2: # Display student
            roll = int(input('Enter student roll number: '))
            student = search_student(roll, students)
            if student:
                display_student(student)
            else:
                print('Student not found')

        case 3: # Search student
            roll = int(input('Enter student roll number: '))
            student = search_student(roll, students)
            if student:
                display_student(student)
            else:
                print('Student not found')

        case 4: # Update student
            roll = int(input('Enter student roll number: '))
            update_student(roll, students)

        case 5: # Save students
            save_students(students)

        case 6: # Load students
            students = load_students()

        case 7: # Exit
            exit_program()
        
        case _:
            print('Invalid choice. Please enter a valid choice.')

