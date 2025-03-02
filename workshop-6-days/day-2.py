# =============================================================
# DAY 2 OF PYTHON PROGRAMMING WORKSHOP
# =============================================================

# Start with a simple project
dict = {
    'marks': {}
}

dict['name'] = input('Enter your name: ') 
dict['age'] = input('Enter your age: ')
dict['rollno'] = input('Enter your rollno: ')
dict['marks']['maths'] = input('Enter your maths marks: ')
dict['marks']['science'] = input('Enter your science marks: ')
dict['marks']['english'] = input('Enter your english marks: ')

total_marks = int(dict['marks']['maths']) + int(dict['marks']['science']) + int(dict['marks']['english'])
percentage = total_marks / 3

result = 'Failed🤦‍♂️'
if percentage >= 40:
    result = 'Passed😀'

print(
    f'''
    ----------------REPORT CARD----------------
    Name: {dict['name']}
    Age: {dict['age']}
    Roll No: {dict['rollno']}

    Maths: {dict['marks']['maths']}
    Science: {dict['marks']['science']}
    English: {dict['marks']['english']}

    Total Marks: {total_marks}
    Percentage: {percentage}
    Result: {result}
    -------------------------------------------
    '''
)

# Loops

# While loop
i = 0
while i < 5:
    print(i)
    i += 1


# For loop
for i in range(5):
    print(i)

# Iterating over a list
list = [1, 2, 3, 4, 5]
for i in list:
    print(i)


# range function
a = range(5)
print(a) # range(0, 5)

# To make a list from range
b = list(range(5))
print(b) # [0, 1, 2, 3, 4]
# similar as

# for with else
for i in range(5):
    print(i)    

else:    
    print('Loop completed')


# break statement
for i in range(5):
    if i == 3:
        break
    print(i)

# continue statement
for i in range(5):
    if i == 3:
        continue
    print(i)

# Print even numbers below 10 using continue
for i in range(10):
    if i % 2 != 0:
        continue
    print(i)

# Print even numbers below 10 using step 2
for i in range(0, 10, 2):
    print(i)

# Print even numbers below 10 using list comprehension
even_numbers = list(range(0, 10, 2))
print(even_numbers)

# pass keyword
for i in range(5):
    pass

# ... is used as a placeholder for future code
for i in range(5):
    ...

# Enumerate function
a = enumerate([1, 2, 3, 4, 5])
print(list(a))

# Enumerate function on for loop
for i, v in enumerate([1, 2, 3, 4, 5]):
    print(i, ':', v)


# Traingular star pattern
n = 5
for i in range(n):
    print('*  ' * (i + 1))

# Traingular reverse star pattern
n = 5
for i in range(n):
    print('*  ' * (n - i))

# Square star pattern
n = 5
for i in range(n):
    print('*  ' * n)

# Factorial of a number using loop
n = 5
fact = 1
for i in range(1, n + 1):
    fact *= i
print(fact)

# Find sum of natural numbers up to num using loop. Take num as input
num = int(input('Enter a number: '))
sum = 0
for i in range(1, num + 1):
    sum += i
print(sum)

# Fibonacci series
num = int(input('Enter a number: '))
fib = [0, 1]
for i in range(2, num):
    fib.append(fib[i - 1] + fib[i - 2])
print(fib)

# Sum digits in a number
number = 567
sum = 0
while number > 0:
    sum += number % 10
    number //= 10
print(sum)

# Sum of digits using the string conversion
number = 567
sum = 0
for i in str(number):
    sum += int(i)
print(sum)

# Check if a number is palinrome or not
number = 12321
temp = number
rev = 0
while number > 0:
    rev = rev * 10 + number % 10
    number //= 10
if temp == rev:
    print(f"{temp} is a palindrome")
else:    
    print(f"{temp} is not a palindrome")


# Check if a number is palinrome or not using the string reverse technique
number = 12321
if str(number) == str(number)[::-1]:
    print(f"{number} is a palindrome")
else:
    print(f"{number} is not a palindrome")
    
    
# Functions
def greet(name):
    print('Hello ' + name)

greet('John')
greet('Doe')
greet('Jane')

# Functions to print sum of two numbers
def add(a, b):
    return a + b

print('The sum of 2 and 3 is:', add(2, 3))
print('The sum of 3 and 3 is:', add(3, 3))
print('The sum of 5 and 3 is:', add(5, 3))

# Doc string
def func():
    '''
    This is a function
    '''
    pass

print(func.__doc__)

# Default arguments in functions
def greet(name='John'):
    print('Hello ' + name)
    
greet()

# Function with a default value and a non-default value
def add(a, b=5):
    return a + b

print('The sum of 2 and 3 is:', add(3))
print('The sum of 3 and 3 is:', add(3, 3))
print('The sum of 5 and 3 is:', add(6))

# variable number of arguments
def add(*args):
    return sum(args)

result = add(1, 2, 3, 4, 5)
print(result)


# variable arguments with some fixed arguments
def add(a, b, *args):
    return a + b + sum(args)

result = add(1, 2, 3, 4, 5)
print(result)

# unpacking
x, y , *unpack = [1, 2, 3, 4, 5]
print(x, y, unpack)