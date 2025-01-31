# 🔀 Python Conditional Statements: Master Decision-Making

Learn to control program flow with `if`, `elif`, `else`, and modern patterns like `match-case`.  

---

## 🧩 Conditional Cheat Sheet  
| Statement | Syntax | Use Case |  
|-----------|--------|----------|  
| `if` | `if condition:` | Single condition check |  
| `if-else` | `if X: ... else: ...` | Binary decisions |  
| `if-elif-else` | `if X: ... elif Y: ... else: ...` | Multi-condition checks |  
| Ternary | `x = a if cond else b` | One-liner assignments |  
| `match-case` (Python 3.10+) | `match value: case X:` | Structural pattern matching |  

---

## 🚨 Common Pitfalls & Fixes  
### 1. **Accidental Assignment in Conditions**  
```python  
if x = 5:  # SyntaxError (use ==)  
```  

### 2. **Truthy/Falsy Confusion**  
```python  
name = ""  
if name:  # Falsy (empty string)  
    print("Hello!")  
```  
✅ **Fix**: Explicit checks:  
```python  
if name is not None:  
    ...  
```  

### 3. **Nested `if` Hell**  
```python  
if a:  
    if b:  
        if c:  
            ...  # Hard to read!  
```  
✅ **Fix**: Use `and`/`elif` or extract logic into functions.  

---

## 🔍 Core Concepts  
### **Truthy/Falsy Values**  
| Falsy | Truthy |  
|-------|--------|  
| `0`, `""`, `None`, `[]`, `{}`, `False` | All non-Falsy values |  

```python  
user_input = input("Enter text: ")  
if user_input:  # True if not empty  
    print("Valid input!")  
```  

### **Short-Circuit Evaluation**  
```python  
# Stops at first False in `and`, first True in `or`  
if user.is_admin or (user.age >= 18 and user.has_id):  
    grant_access()  
```  

---

## 🌍 Real-World Scenarios  
### 1. **Grading System**  
```python  
score = 85  
if score >= 90:  
    grade = "A"  
elif score >= 75:  
    grade = "B"  
elif score >= 50:  
    grade = "C"  
else:  
    grade = "F"  
print(f"Grade: {grade}")  
```  

### 2. **Login Validation**  
```python  
username = input("Username: ")  
password = input("Password: ")  

if username == "admin" and password == "secret":  
    print("Login successful!")  
else:  
    print("Invalid credentials!")  
```  

### 3. **Discount Eligibility**  
```python  
is_member = True  
purchase_amount = 150  

if is_member and purchase_amount > 100:  
    discount = 0.15  
elif purchase_amount > 200:  
    discount = 0.10  
else:  
    discount = 0  
```  

---

## 💡 Advanced Features  
### **Ternary Operator**  
```python  
age = 20  
status = "Adult" if age >= 18 else "Minor"  
```  

### **Structural Pattern Matching (Python 3.10+)**  
```python  
http_status = 404  
match http_status:  
    case 200 | 201:  
        print("Success!")  
    case 404:  
        print("Not Found")  
    case _:  
        print("Unknown error")  
```  

### **Performance Tip: Prefer `elif` Over Nested `if`**  
```python  
# Faster and cleaner  
if x > 0:  
    ...  
elif x == 0:  
    ...  
else:  
    ...  
```  

---

## ✅ Try It Yourself!  
1. **Leap Year Checker**:  
   Write a condition to check if a year is a leap year.  
   ```python  
   year = 2024  
   is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)  
   ```  

2. **Refactor Nested `if`**:  
   Simplify:  
   ```python  
   if user.is_active:  
       if user.has_subscription:  
           print("Access granted")  
   ```  

3. **Type-Checking**:  
   Use `isinstance()` to validate input types.  
   ```python  
   def add(a, b):  
       if isinstance(a, (int, float)) and isinstance(b, (int, float)):  
           return a + b  
       raise TypeError("Numbers only!")  
   ```  

---

## 📚 Resources  
- **Python Docs**: [Control Flow](https://docs.python.org/3/tutorial/controlflow.html)  
- **PEP 636**: [Structural Pattern Matching](https://peps.python.org/pep-0636/)  

---

## ➡️ What’s Next?  
Ready to automate tasks with **Loops**? Head over to [08-loops](/08-loops)!  
