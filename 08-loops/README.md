# 🔁 Python Loops: Automate Repetitive Tasks

Master `for` and `while` loops to iterate efficiently, with real-world examples and performance tips.  

---

## 🧩 Loop Cheat Sheet  
| Loop Type | Syntax | Use Case |  
|-----------|--------|----------|  
| **`for`** | `for item in iterable:` | Iterate over sequences (lists, strings, etc.) |  
| **`while`** | `while condition:` | Repeat until condition becomes `False` |  
| **Nested** | Loop inside another loop | Multi-dimensional data (e.g., matrices) |  
| **Comprehensions** | `[x*2 for x in list]` | Concise list/dict/set creation |  

---

## 🚨 Common Pitfalls & Fixes  
### 1. **Infinite `while` Loops**  
```python  
while True:  # Runs forever!  
    print("Help!")  
```  
✅ **Fix**: Add an exit condition:  
```python  
count = 0  
while count < 5:  
    count += 1  
```  

### 2. **Modifying Lists During Iteration**  
```python  
names = ["Alice", "Bob", "Charlie"]  
for name in names:  
    if "b" in name.lower():  
        names.remove(name)  # Skips elements!  
```  
✅ **Fix**: Iterate over a copy:  
```python  
for name in names.copy():  
    ...  
```  

### 3. **Off-by-One Errors**  
```python  
for i in range(5):  
    print(i)  # 0-4 (not 1-5!)  
```  

---

## 🔍 Core Operations  
### **Loop Control Statements**  
| Statement | Action |  
|-----------|--------|  
| `break` | Exit loop immediately |  
| `continue` | Skip to next iteration |  
| `pass` | Placeholder (do nothing) |  
| `else` | Execute after loop completes normally |  

**Example**:  
```python  
for num in [2, 4, 6]:  
    if num % 2 != 0:  
        break  
else:  
    print("All even!")  
```  

---

## 🌍 Real-World Scenarios  
### 1. **Batch Processing (for loop)**  
```python  
sales = [150, 200, 85, 300]  
total = 0  
for amount in sales:  
    if amount >= 100:  
        total += amount  
print(f"Total high-value sales: ${total}")  
```  

### 2. **User Input Validation (while loop)**  
```python  
password = ""  
while len(password) < 8 or not any(c.isdigit() for c in password):  
    password = input("Enter a strong password: ")  
```  

### 3. **Matrix Operations (nested loops)**  
```python  
matrix = [[1, 2], [3, 4]]  
for row in matrix:  
    for num in row:  
        print(num * 2, end=" ")  # 2 4 6 8  
```  

---

## 💡 Advanced Features  
### **List Comprehensions**  
```python  
# Squares of even numbers  
squares = [x**2 for x in range(10) if x % 2 == 0]  # [0, 4, 16, 36, 64]  
```  

### **Generator Expressions**  
```python  
# Memory-efficient iteration  
large_data = (x * 2 for x in range(10_000))  
```  

### **Enumerate for Index-Value Pairs**  
```python  
colors = ["red", "green", "blue"]  
for idx, color in enumerate(colors, start=1):  
    print(f"{idx}. {color}")  
```  

---

## ✅ Try It Yourself!  
1. **Factorial Calculator**:  
   Use a loop to compute `5! = 5*4*3*2*1`.  

2. **Prime Number Checker**:  
   Write a loop to determine if a number is prime.  

3. **Password Strength Checker**:  
   Validate passwords using:  
   - ≥ 8 characters  
   - At least 1 uppercase, 1 digit, and 1 special character.  

---

## 📚 Resources  
- **Python Docs**: [`for`](https://docs.python.org/3/tutorial/controlflow.html#for-statements) | [`while`](https://docs.python.org/3/reference/compound_stmts.html#while)  
- **Efficiency Guide**: [Use Loop Like a Pro](https://blog.devgenius.io/loop-like-a-pro-97855679e5a7)  

---

## ➡️ What’s Next?  
Ready to modularize code with **Functions & Recursion**? Head over to [09-functions-recursion](/09-functions-recursion)!  
