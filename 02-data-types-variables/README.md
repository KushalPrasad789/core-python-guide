# 📊 Python Data Types & Variables

Learn Python’s core data types, variables, type conversions, and common pitfalls.  

---

## 🧩 Data Types Cheat Sheet  
| Type | Syntax | Mutable? | Example | Use Case |  
|------|--------|----------|---------|----------|  
| **Integer** | `int` | No | `age = 25` | Counting, calculations |  
| **Float** | `float` | No | `price = 19.99` | Measurements, decimals |  
| **String** | `str` | No | `name = "Alice"` | Text processing |  
| **Boolean** | `bool` | No | `is_valid = True` | Flags, conditions |  
| **List** | `list` | Yes | `colors = ["red", "blue"]` | Dynamic collections |  
| **Tuple** | `tuple` | No | `coords = (10, 20)` | Immutable data groups |  
| **Set** | `set` | Yes | `unique = {1, 2, 3}` | Unique items, membership checks |  
| **Dictionary** | `dict` | Yes | `user = {"name": "Alice"}` | Key-value storage |  

---

## 🚨 Common Pitfalls  
### 1. **Type Errors**  
```python  
num = "5"  
total = num + 10  # Error: Can't add str and int!  
```  
**Fix**: Convert types explicitly:  
```python  
total = int(num) + 10  
```  

### 2. **Mutable Default Arguments**  
```python  
def add_item(item, items=[]):  
    items.append(item)  
    return items  

# Repeated calls reuse the same list!  
print(add_item("apple"))  # ["apple"]  
print(add_item("banana"))  # ["apple", "banana"]  
```  
**Fix**: Use `None` as default:  
```python  
def add_item(item, items=None):  
    items = items or []  
    items.append(item)  
    return items  
```  

### 3. **Modifying Lists During Iteration**  
```python  
numbers = [1, 2, 3, 4]  
for num in numbers:  
    if num % 2 == 0:  
        numbers.remove(num)  # Skips elements!  
```  
**Fix**: Iterate over a copy:  
```python  
for num in numbers.copy():  
    if num % 2 == 0:  
        numbers.remove(num)  
```  

---

## 🔄 Type Conversion  
### **Explicit Conversion**  
```python  
age = int("25")  # String ➔ Integer  
price = float("19.99")  # String ➔ Float  
text = str(100)  # Integer ➔ String  
```  

### **Real-World Example**: User Input to Number  
```python  
user_input = input("Enter your age: ")  
age = int(user_input)  # Convert input to integer  
print(f"You’ll be {age + 10} in 10 years!")  
```  

---

## 💡 Type Annotations (Python 3.5+)  
Type hints improve code readability and enable static type checkers like `mypy`:  
```python  
def greet(name: str) -> str:  
    return f"Hello, {name}"  

# Annotating variables  
age: int = 25  
grades: list[float] = [90.5, 85.0, 77.5]  
```  
⚠️ **Note**: Python remains dynamically typed—annotations are optional and not enforced at runtime.  

---

## 🌍 Real-World Scenarios  
### 1. **Shopping Cart (List)**  
```python  
cart = ["apples", "milk", "bread"]  
cart.append("eggs")  # Add item  
cart.pop(1)  # Remove "milk"  
```  

### 2. **Student Record (Dictionary)**  
```python  
student = {  
    "name": "Alice",  
    "courses": ["Math", "Physics"],  
    "grades": {"Math": 90, "Physics": 85}  
}  
print(student["grades"]["Math"])  # 90  
```  

---

## ✅ Try It Yourself!  
1. **Fix the Bug**:  
   ```python  
   # This code raises an error. Fix it!  
   a = "10"  
   b = 20  
   print(a + b)  
   ```  

2. **User Profile**:  
   Create a dictionary `user_profile` with keys: `name`, `email`, `age`.  

3. **List Conversion**:  
   Convert `["10", "20", "30"]` to a list of integers.  

---

## 📚 Resources  
- **Python Docs**: [Built-in Types](https://docs.python.org/3/library/stdtypes.html)  
- **PEP 484**: [Type Hints](https://peps.python.org/pep-0484/)  

---

## ➡️ What’s Next?  
Ready to master **Operators**? Head over to [03-operators](/03-operators)!  
