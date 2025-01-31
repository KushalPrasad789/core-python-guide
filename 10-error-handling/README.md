# 🚨 Python Error Handling: Graceful Recovery & Debugging

Learn to handle exceptions, create custom errors, and write robust code with best practices.  

---

## 🧩 Exception Handling Cheat Sheet  
| Exception | Cause | Example |  
|-----------|-------|---------|  
| `ValueError` | Invalid value for operation | `int("abc")` |  
| `KeyError` | Missing dictionary key | `d["missing"]` |  
| `TypeError` | Incorrect type used | `"a" + 5` |  
| `FileNotFoundError` | File doesn’t exist | `open("missing.txt")` |  
| `IndexError` | Invalid sequence index | `[1,2][3]` |  
| `ZeroDivisionError` | Division by zero | `5 / 0` |  

---

## 🚨 Common Pitfalls & Fixes  
### 1. **Overbroad `except` Clauses**  
```python  
try:  
    risky_operation()  
except:  # Catches all exceptions (even KeyboardInterrupt!)  
    ...  
```  
✅ **Fix**: Catch specific exceptions:  
```python  
except (ValueError, TypeError) as e:  
    ...  
```  

### 2. **Swallowing Exceptions**  
```python  
try:  
    ...  
except ValueError:  
    pass  # Silent failure!  
```  
✅ **Fix**: Log or re-raise:  
```python  
except ValueError as e:  
    logging.error(e)  
    raise  
```  

### 3. **Resource Leaks**  
```python  
file = open("data.txt")  
# If error occurs here, file is never closed!  
file.close()  
```  
✅ **Fix**: Use context managers (`with`):  
```python  
with open("data.txt") as file:  
    ...  
```  

---

## 🔍 Core Concepts  
### **Exception Hierarchy**  
```text  
BaseException  
 ├── KeyboardInterrupt  
 ├── SystemExit  
 └── Exception  
      ├── ValueError  
      ├── TypeError  
      └── ...  
```  

### **Exception Chaining (Python 3.3+)**  
Preserve original traceback when re-raising:  
```python  
try:  
    ...  
except ConnectionError as e:  
    raise RuntimeError("API failed") from e  
```  

### **Logging Exceptions**  
```python  
import logging  

try:  
    ...  
except ValueError as e:  
    logging.exception("Input validation failed: %s", e)  
```  

---

## 🌍 Real-World Scenarios  
### 1. **File Handling with Cleanup**  
```python  
try:  
    with open("data.csv") as file:  
        data = file.read()  
except FileNotFoundError:  
    print("File not found!")  
except UnicodeDecodeError:  
    print("Invalid file encoding!")  
```  

### 2. **API Retry with Exponential Backoff**  
```python  
import time  

def retry_api_call(max_retries=3):  
    retries = 0  
    while retries < max_retries:  
        try:  
            return make_api_request()  
        except ConnectionError:  
            retries += 1  
            time.sleep(2 ** retries)  
    raise RuntimeError("Max retries exceeded")  
```  

### 3. **Input Validation with Custom Exceptions**  
```python  
class InvalidInputError(ValueError):  
    pass  

def validate_age(age):  
    if age < 0:  
        raise InvalidInputError(f"Invalid age: {age}")  
```  

---

## 💡 Advanced Features  
### **Custom Exception Hierarchies**  
```python  
class APIError(Exception):  
    """Base class for API errors."""  

class RateLimitError(APIError):  
    """Raised when API rate limit is exceeded."""  

class TimeoutError(APIError):  
    """Raised when API request times out."""  
```  

### **Exception Groups (Python 3.11+)**  
Handle multiple exceptions simultaneously:  
```python  
try:  
    ...  
except* (ValueError, TypeError) as eg:  
    for e in eg.exceptions:  
        print(f"Caught: {e}")  
```  

### **Assertions for Debugging**  
```python  
def calculate_discount(price):  
    assert price >= 0, "Price cannot be negative!"  
    ...  

# Disable with: python -O script.py  
```  

---

## ✅ Try It Yourself!  
1. **Fix Bare `except`**:  
   Replace `except:` with specific exception handling in:  
   ```python  
   try:  
       user_input = int(input("Enter a number: "))  
   except:  
       print("Error!")  
   ```  

2. **Custom Exception**:  
   Create `InvalidEmailError` for invalid email formats.  

3. **Logging Setup**:  
   Modify the API retry example to log exceptions to a file.  

4. **Context Managers**:  
   Use `contextlib` to safely read/write files.  

---

## 📚 Resources  
- **Python Docs**: [Errors & Exceptions](https://docs.python.org/3/tutorial/errors.html)  
- **Logging Guide**: [Real Python](https://realpython.com/python-logging/)  

---

## ➡️ What’s Next?  
Ready to manage files like a pro? Head over to [11-file-handling](/11-file-handling)!  
