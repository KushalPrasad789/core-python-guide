# 🧩 Python Object-Oriented Programming (OOP): From Basics to Mastery

Master classes, inheritance, polymorphism, and design patterns to write modular, reusable code.  

---

## 🧩 OOP Cheat Sheet  
| Concept | Syntax | Purpose |  
|---------|--------|---------|  
| **Class** | `class MyClass:` | Blueprint for objects |  
| **Object** | `obj = MyClass()` | Instance of a class |  
| **Inheritance** | `class Child(Parent):` | Reuse parent class features |  
| **Polymorphism** | Override methods | Same method name, different behavior |  
| **Encapsulation** | `self._protected` | Hide internal state |  
| **Abstraction** | ABCs with `@abstractmethod` | Define interfaces |  

---

## 🚨 Common Pitfalls & Fixes  
### 1. **Mutable Class Attributes**  
```python  
class Inventory:  
    items = []  # Shared across all instances!  

i1 = Inventory()  
i2 = Inventory()  
i1.items.append("Sword")  # Affects i2.items!  
```  
✅ **Fix**: Use instance attributes in `__init__`:  
```python  
def __init__(self):  
    self.items = []  
```  

### 2. **Overusing Inheritance**  
```python  
class ElectricCar(Car, Battery):  # Fragile hierarchy!  
    ...  
```  
✅ **Fix**: Prefer composition:  
```python  
class ElectricCar:  
    def __init__(self):  
        self.engine = Engine()  
        self.battery = Battery()  
```  

### 3. **Misunderstanding `self`**  
```python  
class User:  
    def logout():  # Missing self!  
        ...  
```  
✅ **Fix**: Always include `self` in instance methods.  

---

## 🔍 Core Concepts  
### **OOP vs. Procedural Programming**  
| OOP | Procedural |  
|-----|------------|  
| Data & behavior bundled in objects | Functions operate on separate data |  
| Easier code reuse via inheritance | Reusability via functions/modules |  
| Models real-world entities | Linear, step-by-step execution |  

### **Duck Typing**  
```python  
class Duck:  
    def quack(self): print("Quack!")  

class Person:  
    def quack(self): print("I’m quacking!")  

def make_sound(obj):  
    obj.quack()  

make_sound(Duck())  # Quack!  
make_sound(Person())  # I’m quacking!  
```  

### **Design Patterns**  
#### **Singleton**  
```python  
class Singleton:  
    _instance = None  
    def __new__(cls):  
        if not cls._instance:  
            cls._instance = super().__new__(cls)  
        return cls._instance  

s1 = Singleton()  
s2 = Singleton()  
print(s1 is s2)  # True  
```  

#### **Factory**  
```python  
class ButtonFactory:  
    @staticmethod  
    def create_button(type):  
        if type == "windows":  
            return WindowsButton()  
        elif type == "mac":  
            return MacButton()  
```  

---

## 🌍 Real-World Scenarios  
### 1. **Banking System (Inheritance)**  
```python  
class Account:  
    def __init__(self, balance):  
        self.balance = balance  

class SavingsAccount(Account):  
    def add_interest(self, rate):  
        self.balance *= (1 + rate)  

class CheckingAccount(Account):  
    def deduct_fee(self, fee):  
        self.balance -= fee  
```  

### 2. **GUI Framework (Polymorphism)**  
```python  
class Widget:  
    def draw(self):  
        pass  

class Button(Widget):  
    def draw(self):  
        print("Rendering button...")  

class TextField(Widget):  
    def draw(self):  
        print("Rendering text field...")  

# All widgets can be drawn uniformly  
for widget in [Button(), TextField()]:  
    widget.draw()  
```  

### 3. **E-commerce Payment Gateways (Abstraction)**  
```python  
from abc import ABC, abstractmethod  

class PaymentGateway(ABC):  
    @abstractmethod  
    def process_payment(self, amount):  
        pass  

class CreditCardGateway(PaymentGateway):  
    def process_payment(self, amount):  
        print(f"Processing ${amount} via credit card...")  

class PayPalGateway(PaymentGateway):  
    def process_payment(self, amount):  
        print(f"Processing ${amount} via PayPal...")  
```  

---

## 💡 Advanced Features  
### **Type Annotations (Python 3.9+)**  
```python  
from typing import Generic, TypeVar  

T = TypeVar('T')  

class Box(Generic[T]):  
    def __init__(self, item: T):  
        self.item = item  

box = Box[int](10)  # Explicit type  
```  

### **Magic Methods**  
```python  
class Vector:  
    def __init__(self, x, y):  
        self.x = x  
        self.y = y  

    def __add__(self, other):  
        return Vector(self.x + other.x, self.y + other.y)  

    def __str__(self):  
        return f"Vector({self.x}, {self.y})"  

v = Vector(2, 3) + Vector(4, 5)  
print(v)  # Vector(6, 8)  
```  

### **Dataclasses (Python 3.7+)**  
```python  
from dataclasses import dataclass  

@dataclass  
class Product:  
    id: int  
    name: str  
    price: float  

p = Product(1, "Laptop", 999.99)  
```  

---

## ✅ Try It Yourself!  
1. **Fix Shared Mutable Attribute**:  
   Modify the `Inventory` class to prevent shared `items` across instances.  

2. **Shape Hierarchy**:  
   Create `Circle` and `Rectangle` classes with `area()` method.  

3. **Singleton Logger**:  
   Implement a logging class that allows only one instance.  

---

## 📚 Resources  
- **Python Docs**: [Classes](https://docs.python.org/3/tutorial/classes.html)  
- **Design Patterns**: [Refactoring.Guru](https://refactoring.guru/design-patterns/python)  

---

## ➡️ What’s Next?  
Ready to organize code into modules? Head over to [13-modules-packages](/13-modules-packages)!  
