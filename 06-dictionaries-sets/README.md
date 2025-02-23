# 🗂️ Python Dictionaries & Sets: Master Key-Value Pairs and Unique Collections

Learn to leverage dictionaries for structured data and sets for unique elements with practical examples.  

---

## 🧩 Dictionaries vs. Sets Cheat Sheet  
| Feature | Dictionary (`dict`) | Set (`set`) |  
|---------|----------------------|-------------|  
| **Purpose** | Key-value pairs (e.g., user profiles) | Unique elements (e.g., tags) |  
| **Syntax** | `{key: value}` | `{item1, item2}` |  
| **Mutability** | Keys: Immutable<br>Values: Mutable | Mutable (except `frozenset`) |  
| **Lookup Speed** | O(1) for keys (ultra-fast) | O(1) for membership checks |  
| **Order** | Insertion order preserved (Python 3.7+) | Unordered |  

---

## 🚨 Common Pitfalls  
### 1. **Key Errors in Dictionaries**  
```python  
user = {"name": "Alice"}  
print(user["age"])  # KeyError: 'age' not found!  
```  
✅ **Fix**: Use `.get()` with a default:  
```python  
age = user.get("age", 25)  # Returns 25 if "age" missing  
```  

### 2. **Mutable Keys in Dictionaries**  
```python  
invalid_dict = {["a", "b"]: "value"}  # Error: Lists can’t be keys!  
```  
✅ **Fix**: Use tuples or strings as keys.  

### 3. **Set Duplicate Entries**  
```python  
nums = {1, 2, 2, 3}  # Duplicates auto-removed: {1, 2, 3}  
```  

---

## 🔍 Core Operations  
### **Dictionary Methods**  
| Method | Action | Example |  
|--------|--------|---------|  
| `.keys()` | Get all keys | `user.keys() → ["name", "age"]` |  
| `.values()` | Get all values | `user.values() → ["Alice", 25]` |  
| `.items()` | Get key-value pairs | `user.items() → [("name", "Alice"), ...]` |  
| `.setdefault()` | Safe key access | `user.setdefault("city", "Paris")` |  

### **Set Operations**  
| Operation | Syntax | Example |  
|-----------|--------|---------|  
| Union | `set1 \| set2` | `{1,2} | {2,3} → {1,2,3}` |  
| Intersection | `set1 & set2` | `{1,2} & {2,3} → {2}` |  
| Difference | `set1 - set2` | `{1,2} - {2,3} → {1}` |  

---

## 🌍 Real-World Scenarios  
### 1. **User Profile (Dictionary)**  
```python  
user = {  
    "id": 101,  
    "name": "Alice",  
    "roles": {"admin", "editor"}  
}  
# Add new key  
user["email"] = "alice@mail.com"  
```  

### 2. **Data Deduplication (Set)**  
```python  
duplicates = [1, 2, 2, 3, 3, 3]  
unique = set(duplicates)  # {1, 2, 3}  
```  

### 3. **JSON Serialization (Dictionary)**  
```python  
import json  
config = {"host": "localhost", "port": 8080}  
json_data = json.dumps(config)  # '{"host": "localhost", "port": 8080}'  
```  

---

## 💡 Advanced Features  
### **Frozen Sets (Immutable)**  
```python  
permissions = frozenset(["read", "write"])  
# permissions.add("execute")  # Error: Frozen sets are immutable!  
```  

### **Type Annotations (Python 3.9+)**  
```python  
from typing import Dict, Set  

def process_data(  
    users: Dict[int, str],  
    tags: Set[str]  
) -> Dict[int, Set[str]]:  
    return {1: {"admin"}, 2: {"editor"}}  
```  

### **Performance Tip: Dictionary Lookups vs. Lists**  
```python  
# Faster with dictionaries!  
users_dict = {101: "Alice", 102: "Bob"}  
users_list = [101, "Alice", 102, "Bob"]  

# Dict lookup: O(1)  
print(users_dict[101])  # "Alice"  

# List "lookup": O(n)  
index = users_list.index(101)  
print(users_list[index + 1])  # "Alice"  
```  

---

## ✅ Try It Yourself!  
1. **Merge Dictionaries**:  
   Combine `{"a": 1}` and `{"b": 2}` into `{"a": 1, "b": 2}`.  

2. **Find Common Elements**:  
   Use sets to find common friends between `alice_friends = {"Bob", "Charlie"}` and `bob_friends = {"Charlie", "Diana"}`.  

3. **Convert Nested Lists to Dictionaries**:  
   Turn `[["name", "Alice"], ["age", 25]]` into `{"name": "Alice", "age": 25}`.  

---

## 📚 Resources  
- **Python Docs**: [Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) | [Sets](https://docs.python.org/3/tutorial/datastructures.html#sets)  
- **Advanced Structures**: [`collections` Module](https://docs.python.org/3/library/collections.html)  

---

## ➡️ What’s Next?  
Ready to master **Conditional Statements**? Head over to [07-conditional-statements](/07-conditional-statements)!  
