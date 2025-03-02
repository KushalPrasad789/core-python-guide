# =============================================================
# DAY 1 OF PYTHON PROGRAMMING WORKSHOP
# =============================================================

# OBJECT ORIENTED PROGRAMMING
# ------------------------------------

# Creating a class student
class Student:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    
    
    # get_name method for student class
    def get_name(self):
        return self.name
    
    # update_address method to update the address of the object
    def update_address(self, address):
        self.address = address
    
    # Representation of the object of the class
    def __repr__(self):
        return f"Student(name={self.name}, age={self.age}, address={self.address})"
    
    # __str__() Dunder method
    def __str__(self):
        return self.name
    
    # Define the addition operator
    def __add__(self, other):
        return self.age + other.age
    
# Creating a object of class Student
student1 = Student('Abhinav', 39, 'Kathmandu')
print(student1.get_name())

# Creating more objects.
# You can create any number of objects 
student2 = Student('John', 25, 'New York')
student3 = Student('Alice', 30, 'London')

# Calling the get_name method in objects
print(student2.get_name())
print(student3.get_name())

# We can also access the attributes without any methods
print(student1.name)
print(student1.age)
print(student1.address)
# Simillary you can do it for all other objects

# Update the address of the student
student1.update_address('London')
print(student1.address)

# Printing the objects
print(student1)
print(student2)

# Finding the lengths of object
print(len(student1))
print(len(student2))

# Adding two students
print(student1 + student2)

# ================================================================

# Write a class Students with the attributes of the student.
# Add the __init__ method to initialize the Student objects.
# Create a list of 3 students by taking input from user
# Write a method to change the address of the object using name.

# ------------------------------------------------------------------
# Creating class student
class Students:
    # Constructor
    def __init__(self, name, age, roll, address):
        self.name = name
        self.age = age
        self.roll = roll
        self.address = address
    
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Roll: {self.roll}, Address: {self.address}"
    
# Method for the updation of address using the name of object
def update_address(name, address):
    for student in students_list:
        if student.name == name:
            student.address = address
            break
        
# Function to create a list of 5 students by taking input from user
def create_students():
    students_list = []
    for _ in range(3):
        print('-' * 35)
        print(f'Enter data for student{_ + 1}: ')
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        roll = int(input("Enter roll number: "))
        address = input("Enter address: ")
        students_list.append(Students(name, age, roll, address))
    return students_list

# Create the list of students
students_list = create_students()

# Print the data after the updation of addressess is completed
print('*' * 35)
print('Current data of students: ')
for _ in students_list:
    print(_)

# Example of updating address
print('-' * 35)
print('It\' time to change the address:')
name = input('Enter name whose address is to be updated: ')
new_address = input('Enter new address: ')
update_address(name, new_address)

# Print the data after the updation of addressess is completed
print('*' * 35)
print('Current data of students: ')
for _ in students_list:
    print(_)
    
# ====================================================================


# =====================================================================
# WAP to add two vectors using the Vector class
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector(x={self.x}, y={self.y})"

# Creating two vector objects
vector1 = Vector(2, 3)
vector2 = Vector(4, 5)

# Adding two vectors
result_vector = vector1 + vector2

# Printing the result
print(result_vector)

# =================================================================================

# INHERITANCE IN PYTHON
#----------------------------------
# Creating a parent class Animal
class Animal:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
        
        def speak(self):
            return 'Ixcvxcvcxcv'
        
        def wag_tail(self):
            return 'waiging tail'
        
# Inheriting Dog class from the Animal class
class Dog(Animal):
    def __init__(self, name, age, color, breed):
        super().__init__(name, age, color)
        self.breed = breed
        
    def speak(self):
        return 'bark'

# Inheriting Cat class from the Animal class
class Cat(Animal):
    def __init__(self, name, age, color, breed):
        super().__init__(name, age, color)
        self.breed = breed
        
    def speak(self):
        return 'meow'

# Creating objects from the derived classes
cat1 = Cat('kitty', 2, 'whit', 'persion')
cat1.speak()

dog1 = Dog('tommy', 2, 'black', 'german')
dog1.speak()

# ==============================================================


# =================================================================
# Example of Inheritance

# Defining a parent class CellPhone
class CellPhone:
    def __init__(self, name):
        self.name = name
        
    def call():
        print('I can make a call')
        
# Inheriting the class SmartPhone from class CellPhone
class SmartPhone(CellPhone):
    def __init__(self, name, brand):
        super().__init__(name)
        self.brand = brand
        
    def click_pic():
        print('I can click a picture')
# The smartphone can both call and click pictures
    # call() inherited from the parent class CellPhone
    # click_pic() is added after the inheritance
    
# CellPhone object
cell_phone = CellPhone('Nokia')
cell_phone.call()

# SmartPhone object
smart_phone = SmartPhone('Samsung', 'A22')
smart_phone.call()
smart_phone.click_pic()

# ===========================================================
# Diamond inheritance problem

class Root:
    f = 'root'

class A(Root):
    f = 'A'
    
class B(Root):
    f = 'B'
    
class C (A, B):
    f = 'C'
    
# Object of class C
c = C()
print(c.f)
print([cls for cls in C. __mro__])
print([cls.__name__ for cls in C. __mro__])

# ================================================================

# ==================================================================
# List comprehension
print([i for i in range(10)])


# ==================================================================
# Print even numbers from 0 to 50 using list comprehension
print([i for i in range(50) if i % 2 == 0])

