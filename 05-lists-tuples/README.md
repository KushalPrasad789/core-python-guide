# 📚 Python Lists & Tuples: The Complete Guide
Learn the differences, use cases, and best practices for Python’s two most versatile sequence types.

---

## 🧩 Lists vs. Tuples Cheat Sheet
| Feature | List | Tuple |
|---------|------|-------|
| **Mutability** | Mutable (can be modified) | Immutable (fixed after creation) |
| **Syntax** | Square brackets `[ ]` | Parentheses `( )` |
| **Performance** | Slightly slower (dynamic) | Faster (static) |
| **Use Case** | Dynamic data (e.g., shopping cart) | Fixed data (e.g., database config) |
| **Methods** | `.append()`, `.sort()`, `.pop()`, etc. | `.count()`, `.index()` only |

---

## 🚨 Common Pitfalls
### 1. **Accidental Tuple Modification**
```python
coordinates = (10, 20)
coordinates[0] = 5  # Error: Tuples are immutable!
```
✅ **Fix**: Use a list if you need mutability.

### 2. **Shallow Copies in Lists**
```python
list1 = [[1, 2], [3, 4]]
list2 = list1.copy()
list2[0][0] = 99
print(list1)  # [[99, 2], [3, 4]] (both changed!)
```
✅ **Fix**: Use `copy.deepcopy()` for nested structures.

---
## 🔍 Core Operations
### **List Methods Cheat Sheet**
| Method | Action | Example |
|--------|--------|---------|
| `.append(x)` | Add item to end | `[1,2].append(3) → [1,2,3]` |
| `.insert(i, x)` | Insert at index `i` | `[1,3].insert(1,2) → [1,2,3]` |
| `.remove(x)` | Delete first `x` | `[1,2,2].remove(2) → [1,2]` |
| `.sort()` | Sort in-place | `[3,1,2].sort() → [1,2,3]` |
| `list[start:end]` | Slice sublist | `[1,2,3,4][1:3] → [2,3]` |

### **Tuple Unpacking**
```python
# Swap variables
a, b = 5, 10
a, b = b, a  # a=10, b=5
# Function returning multiple values
def get_user():
    return ("Alice", 25, "alice@mail.com")
name, age, email = get_user()
```

---

## 🌍 Real-World Scenarios
### 1. **Shopping Cart (List)**
```python
cart = ["apples", "milk"]
cart.append("bread")  # Add item
cart.remove("milk")   # Remove item
print(f"Cart: {', '.join(cart)}")  # Cart: apples, bread
```

### 2. **RGB Color Config (Tuple)**
```python
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
def set_color(color: tuple):
    print(f"R: {color[0]}, G: {color[1]}, B: {color[2]}")
```

---

## 💡 Advanced Features
### **Type Annotations (Python 3.9+)**
```python
from typing import List, Tuple
def process_data(
    items: List[str],
    metadata: Tuple[str, int]
) -> Tuple[List[str], int]:
    return (items, len(items))
```

### **List Comprehensions**
```python
# Generate squares of even numbers
squares = [x**2 for x in range(10) if x % 2 == 0]
# [0, 4, 16, 36, 64]
```

---

## ✅ Try It Yourself!
1. **Fix the Bug**:
   ```python
   # Why does this fail? Fix it!
   config = ("localhost", 8080)
   config[1] = 8000
   ```

2. **Merge Lists**:
   Combine `[1, 2, 3]` and `[4, 5, 6]` into `[1,2,3,4,5,6]` without using `+`.

3. **Tuple to Dictionary**:
   Convert `(("name", "Alice"), ("age", 25))` into `{"name": "Alice", "age": 25}`.

---

## 📚 Resources
- **Python Docs**: [Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists) | [Tuples](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)
- **Efficiency Guide**: [When to Use Lists and Tuples](https://stackoverflow.com/questions/1708510/list-vs-tuple-when-to-use-each)

---

## ➡️ What’s Next?
Ready to master **Dictionaries & Sets**? Head over to [06-data-structures-dicts-sets](/06-data-structures-dicts-sets)!
