# 🎯 Python Operators: Basics to Advanced

Master Python operators for efficient calculations, comparisons, and logical workflows.  

---

## 🧩 Operator Cheat Sheet  
| Category | Operator | Syntax | Example |  
|----------|----------|--------|---------|  
| **Arithmetic** | `+`, `-`, `*`, `/`, `//`, `%`, `**` | `a + b` | `5 + 3 → 8` |  
| **Comparison** | `==`, `!=`, `>`, `<`, `>=`, `<=` | `a == b` | `5 == 3 → False` |  
| **Logical** | `and`, `or`, `not` | `x and y` | `True and False → False` |  
| **Bitwise** | `&`, `\|`, `^`, `~`, `<<`, `>>` | `a & b` | `5 & 3 → 1` |  
| **Assignment** | `=`, `+=`, `-=`, `*=` | `a += 5` | `a = 10 → 15` |  
| **Identity** | `is`, `is not` | `a is b` | `"hi" is "hi" → True` |  
| **Membership** | `in`, `not in` | `x in list` | `2 in [1,2,3] → True` |  

---

## 🚨 Common Pitfalls  
### 1. **Misusing `is` for Value Comparison**  
```python  
a = 256  
b = 256  
print(a is b)  # True (due to interning)  

c = 257  
d = 257  
print(c is d)  # False (for larger integers)  
```  
✅ **Fix**: Use `==` for value checks: `print(a == b)`.  

### 2. **Operator Precedence Errors**  
```python  
result = 5 + 3 * 2  # 11, not 16!  
```  
✅ **Fix**: Use parentheses: `(5 + 3) * 2 → 16`.  

### 3. **Chained Comparisons**  
```python  
# Valid in Python!  
if 0 < age <= 100:  
    print("Valid age")  
```  

---

## 🔄 Real-World Scenarios  
### 1. **Shopping Cart Total (Arithmetic)**  
```python  
price = 49.99  
quantity = 3  
discount = 0.15  
total = (price * quantity) * (1 - discount)  
print(f"Total: ${total:.2f}")  # $127.47  
```  

### 2. **User Authentication (Logical)**  
```python  
has_valid_email = True  
has_password = False  
access = has_valid_email and has_password  # False  
```  

### 3. **Bitmask Permissions (Bitwise)**  
```python  
READ = 0b100  
WRITE = 0b010  
EXECUTE = 0b001  

user_perms = READ | WRITE  
print(bin(user_perms))  # 0b110 (READ + WRITE)  
```  

---

## ✅ Try It Yourself!  
1. **Fix the Bug**:  
   ```python  
   # Why does this return False?  
   a = 10  
   b = 10.0  
   print(a is b)  
   ```  

2. **Calculate BMI**:  
   Use an arithmetic operators to compute BMI  

3. **Check Username Validity**:  
   Use `and`/`or` to validate:  
   - Length ≥ 6  
   - Contains letters and numbers  

---

## 📚 Resources  
- **Python Docs**: [Expressions](https://docs.python.org/3/reference/expressions.html)  
- **Operator Precedence**: [Order of Operations](https://docs.python.org/3/reference/expressions.html#operator-precedence)  

---

## ➡️ What’s Next?  
Ready to dive into **Control Flow**? Head over to [04-conditional-statements](/04-conditional-statements)!  
