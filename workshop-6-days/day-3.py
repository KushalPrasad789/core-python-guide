# =============================================================
# DAY 3 OF PYTHON PROGRAMMING WORKSHOP
# =============================================================

# Use of *args in Python
def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

# WAP to find the sum of 5 numbers from a list using *args
def add(*args):
    return sum(args)

l = []

for i in range(5):
    l.append(int(input('Enter a number: ')))

print(add(*l))
print(add(l[0], l[1], l[2], l[3], l[4])) # Same as above

# Use of **kwargs in Python
def greet(**kwargs):
    for k, v in kwargs.items():
        print(k, ':', v)

greet(name='John', age=25, city='New York')



# ======================================================================================
# ======================================================================================

# Make a student management system using functions
# 1. Add student function
def add_student():
    name = input('Enter student name: ')
    age = int(input('Enter student age: '))
    city = input('Enter student city: ')
    return {'name': name, 'age': age, 'city': city} # Return a dictionary

# 2. Display student function
def display_student(student):
    print('Name:', student['name'])
    print('Age:', student['age'])
    print('City:', student['city'])

# 3. Search student function
def search_student(name, students):
    for student in students: # Iterate through the list of students to find the student
        if student['name'] == name:
            return student # Return the student if found
    return None # Return None if student not found

# 4. Update student function
def update_student(name, students):
    student = search_student(name, students) # Search for the student 
    if student:
        # student['name'] = input('Enter student name: ')  # Treat the name as a primary key so no need to update it
        student['age'] = int(input('Enter student age: '))
        student['city'] = input('Enter student city: ')
    else:
        print('Student not found')

# 5. Delete student function
def delete_student(name, students):
    student = search_student(name, students) # Search for the student
    if student:
        students.remove(student)
        print(f'{student['name']} removed successfully.')
    else:
        print('Student not found')

# 6. Exit program function
def exit_program():
    print('Exiting program')
    exit()

students = [] # Empty list for the students

# Main program
while True:
    # Dispaly the menu
    print('='*20)
    print('1. Add student')
    print('2. Display student')
    print('3. Search student')
    print('4. Update student')
    print('5. Delete student')
    print('6. Exit')
    print('-'*20)

    choice = int(input('Enter your choice: '))

    if choice == 1: # Add student
        students.append(add_student())

    elif choice == 2: # Display student
        print('Details for all students is as follows: ')
        for student in students:
            print('-'*20)
            print(f'Details for {student['name']}')
            display_student(student)

    elif choice == 3: # Search student
        name = input('Enter student name: ')
        student = search_student(name, students)
        if student: # If student is found
            display_student(student)
        else: # If student is not found
            print('Student not found')

    elif choice == 4: # Update student
        name = input('Enter student name: ')
        update_student(name, students)

    elif choice == 5:# Delete student
        name = input('Enter student name: ')
        delete_student(name, students)

    elif choice == 6: # Exit program
        print('-'*20)
        exit_program()

    else:
        print('Invalid choice')

    print() # For some additional space



# ======================================================================
# ======================================================================


# Importing modules
import random

print(random.randint(0, 2))

# Using alias
import random as rd
print(rd.randint(0, 5))

# from keyword
from random import randint as r

print(r(0, 2))


# ===================================================================
# ===================================================================

# Scissors, Paper , Rock game

import random # For random selection of integer

wining_conditions = [1, -2] # Output from the (user_input - machine_input)
choices = ['paper', 'scissors', 'rock']

# Function to get the user input
def get_user_choice():
    while True:
        user_input = input("Enter your choice (paper, scissors, rock): ").lower()
        if user_input in choices:
            return choices.index(user_input)
        else:
            print("Invalid choice. Please try again.")

# Function to get the machine input
def get_machine_choice():
    return random.randint(0, 2)

# Function to determine the winner
def determine_winner(user_choice, machine_choice):
    result = user_choice - machine_choice
    if result in wining_conditions:
        return "User wins!"
    elif result == 0:
        return "It's a tie!"
    else:
        return "Machine wins!"

# Function to start game play
def play_game():
    user_choice = get_user_choice()
    machine_choice = get_machine_choice()
    print(f"User choice: {choices[user_choice]}")
    print(f"Machine choice: {choices[machine_choice]}")
    print(determine_winner(user_choice, machine_choice))

# Call the function to start the game play
while True:
    play_game()

    print('=' * 30)

# ==========================================================================
# ===========================================================================


# try and except

# While writing a program we face some errors
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result = num1 / num2
print('Result:', result)
# This programs give error while num2 is 0

# These errors can be handled by following method
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print('Result:', result)
except ValueError:
    print('Invalid input. Please enter numbers only.')
except ZeroDivisionError:
    print('Cannot divide by 0')

    
# For handling all types of exceptions
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print('Result:', result)
except Exception as e:
    print(e)
    
