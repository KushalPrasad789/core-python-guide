# 📝 Python Strings: From Basics to Advanced

Master Python strings with syntax, methods, real-world use cases, and common pitfalls.  

---

## 🧩 String Basics Cheat Sheet  
| Feature | Syntax | Example |  
|---------|--------|---------|  
| **Single Quotes** | `'text'` | `'Python'` |  
| **Double Quotes** | `"text"` | `"Hello"` |  
| **Triple Quotes** | `'''text'''` or `"""text"""` | Multi-line strings |  
| **Escape Sequences** | `\n`, `\t`, `\"`, `\\` | `"Line 1\nLine 2"` |  
| **Raw Strings** | `r"text"` | `r"C:\path"` (ignores escapes) |  
| **Indexing** | `s[index]` | `"Python"[0] → "P"` |  
| **Slicing** | `s[start:end:step]` | `"Python"[0:3] → "Pyt"` |  

---

## 🚨 Common Pitfalls  
### 1. **String Immutability**  
```python  
s = "hello"  
s[0] = "H"  # Error: Strings are immutable!  
```  
✅ **Fix**: Create a new string.  
```python  
s = "H" + s[1:]  # "Hello"  
```  

### 2. **Encoding/Decoding Issues**  
```python  
# Bytes vs. Unicode  
data = b"Hello"  # Bytes  
text = "Hello"    # Unicode  
print(data.decode("utf-8") == text)  # True  
```  

---

## 🔍 String Methods Cheat Sheet  
| Method | Action | Example |  
|--------|--------|---------|  
| `s.upper()` | Uppercase | `"Hi".upper() → "HI"` |  
| `s.lower()` | Lowercase | `"Hi".lower() → "hi"` |  
| `s.strip()` | Remove whitespace | `" Hi ".strip() → "Hi"` |  
| `s.split(delim)` | Split into list | `"a,b,c".split(",") → ["a","b","c"]` |  
| `s.join(list)` | Join list into string | `",".join(["a","b"]) → "a,b"` |  
| `s.replace(old, new)` | Replace substring | `"Hello".replace("e", "a") → "Hallo"` |  
| `s.find(sub)` | Find substring index | `"Python".find("th") → 2` |  

---

## 🌍 Real-World Scenarios  
### 1. **Cleaning User Input**  
```python  
user_input = "  ALICE@gmail.com  "  
clean_email = user_input.strip().lower()  
print(clean_email)  # "alice@gmail.com"  
```  

### 2. **Generating Formatted Reports (f-strings)**  
```python  
name = "Alice"  
score = 95  
report = f"""  
Student: {name.upper()}  
Score: {score}/100  
Status: {"Pass" if score >= 50 else "Fail"}  
"""  
print(report)  
```  

---

## 💡 Advanced String Features  
### **Type Annotations (Python 3.5+)**  
```python  
def reverse_string(s: str) -> str:  
    return s[::-1]  

print(reverse_string("Python"))  # "nohtyP"  
```  

### **Raw Strings for File Paths**  
```python  
path = r"C:\Users\Alice\Documents"  # No escape issues!  
```  

---

## ✅ Try It Yourself!  
1. **Palindrome Check**:  
   Write a function to check if a string reads the same backward.  
   ```python  
   def is_palindrome(s: str) -> bool:  
       return s == s[::-1]  
   ```  

2. **Parse CSV String**:  
   Convert `"name,age,email\nAlice,25,alice@mail.com"` into a list of dictionaries.  

3. **Password Validator**:  
   Use string methods to check if a password has:  
   - ≥ 8 characters  
   - At least one uppercase and one digit  

---

## 📚 Resources  
- **Python Docs**: [String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)  
- **f-strings Guide**: [Real Python](https://realpython.com/python-f-strings/)  

---

## ➡️ What’s Next?  
Ready to explore **Lists & Tuples**? Head over to [05-data-structures-lists-tuples](/05-data-structures-lists-tuples)!  
