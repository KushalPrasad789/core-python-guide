# 🛠️ Python Functions & Recursion: Modularize and Optimize Code

Master function design, recursion, closures, and decorators for clean, reusable, and efficient Python code.  

---

## 🧩 Function Cheat Sheet  
| Feature | Syntax | Use Case |  
|---------|--------|----------|  
| **Positional Args** | `def func(a, b):` | Fixed order of inputs |  
| **Keyword Args** | `func(a=1, b=2)` | Explicit parameter naming |  
| **Default Args** | `def func(a=0):` | Fallback values |  
| **`*args`** | `def func(*args):` | Variable positional args |  
| **`**kwargs`** | `def func(**kwargs):` | Variable keyword args |  
| **Lambda** | `lambda x: x*2` | Anonymous single-expression functions |  

---

## 🚨 Common Pitfalls & Fixes  
### 1. **Mutable Default Arguments**  
```python  
def append_to(item, items=[]):  
    items.append(item)  
    return items  

print(append_to(1))  # [1]  
print(append_to(2))  # [1, 2] (Same list reused!)  
```  
✅ **Fix**: Use immutable defaults (e.g., `None`):  
```python  
def append_to(item, items=None):  
    items = items or []  
    ...  
```  

### 2. **Infinite Recursion**  
```python  
def countdown(n):  
    countdown(n-1)  # No base case!  
```  
✅ **Fix**: Define a base case:  
```python  
def countdown(n):  
    if n <= 0: return  
    countdown(n-1)  
```  

### 3. **Accidental Shadowing**  
```python  
total = 100  
def calculate():  
    total = 0  # Shadows global "total"  
    ...  
```  
✅ **Fix**: Use `global` or rename variables.  

---

## 🔍 Core Concepts  
### **Scope Hierarchy**  
```text
Global → Nonlocal (enclosing) → Local
```  
**Example**:  
```python  
x = "global"  
def outer():  
    x = "nonlocal"  
    def inner():  
        nonlocal x  # Refers to outer's x  
        x = "local"  
    inner()  
    print(x)  # "local"  
outer()  
```  

### **Closures**  
Functions that retain access to variables from their enclosing scope:  
```python  
def counter():  
    count = 0  
    def increment():  
        nonlocal count  
        count += 1  
        return count  
    return increment  

c = counter()  
print(c(), c())  # 1, 2  
```  

---

## 🌍 Real-World Scenarios  
### 1. **API Request Handler (`*args`, `**kwargs`)**  
```python  
def api_call(url, *params, **headers):  
    print(f"Fetching {url} with params={params} and headers={headers}")  

api_call("https://api.com", "data", retries=3, auth="Bearer XYZ")  
```  

### 2. **Recursive Directory Traversal**  
```python  
import os  

def list_files(path):  
    for entry in os.listdir(path):  
        full_path = os.path.join(path, entry)  
        if os.path.isdir(full_path):  
            list_files(full_path)  # Recursion!  
        else:  
            print(full_path)  
```  

### 3. **Decorators for Logging**  
```python  
def log_time(func):  
    import time  
    def wrapper(*args, **kwargs):  
        start = time.time()  
        result = func(*args, **kwargs)  
        print(f"{func.__name__} took {time.time() - start:.2f}s")  
        return result  
    return wrapper  

@log_time  
def heavy_computation():  
    return sum(i*i for i in range(10**6))  
```  

---

## 💡 Advanced Features  
### **Type Hints (Python 3.5+)**  
```python  
from typing import Optional  

def greet(name: str, age: Optional[int] = None) -> str:  
    return f"Hello, {name}" if age is None else f"{name} is {age} years old"  
```  

### **Decorator Chaining**  
```python  
def bold(func):  
    def wrapper(): return f"<b>{func()}</b>"  
    return wrapper  

def italic(func):  
    def wrapper(): return f"<i>{func()}</i>"  
    return wrapper  

@bold  
@italic  
def hello(): return "Hello"  

print(hello())  # <b><i>Hello</i></b>  
```  

### **Recursion Limits**  
```python  
import sys  
sys.setrecursionlimit(3000)  # Default is 1000  
```  

---

## ✅ Try It Yourself!  
1. **Recursive Binary Search**:  
   Implement a function to find an item in a sorted list using recursion.  

2. **Execution Time Decorator**:  
   Write a decorator to log how long a function takes to run.  

3. **Fix the Closure**:  
   Debug this code to make the counter work:  
   ```python  
   def counter():  
       count = 0  
       return lambda: count += 1  # Error!  
   ```  

---

## 📚 Resources  
- **Python Docs**: [Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)  
- **Recursion Guide**: [Real Python](https://realpython.com/python-recursion/)  

---

## ➡️ What’s Next?  
Ready to handle errors gracefully? Head over to [10-error-handling](/10-error-handling)!  
