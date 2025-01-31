# 🐍 Introduction to Python

Welcome to the **Introduction to Python**! This section covers Python's history, a quick installation guide, and writing your first program. Let’s dive in!

---

## 📜 History of Python
### Key Milestones
- **1991**: Created by **Guido van Rossum** to emphasize code readability.
- **2000**: Python 2.0 released (legacy version, now deprecated).
- **2008**: Python 3.0 released (backward-incompatible, current standard).
- **2020**: Python 3.9 introduced faster updates and new syntax features.

```text
Timeline:
1991 🡪 Python 1.0
2000 🡪 Python 2.0
2008 🡪 Python 3.0
2023 🡪 Python 3.11 (Latest)
```

💡 **Fun Fact**: Python is named after the British comedy series *Monty Python*!

---

## 🛠 Quick Installation Guide
1. **Download Python**: Visit [python.org/downloads](https://www.python.org/downloads/).
2. **Install**:
   - Check **"Add Python to PATH"** during setup (critical for terminal access).
3. **Verify**:
   ```bash
   python --version
   # Output: Python 3.x.x
   ```

🔗 *Detailed installation steps are in the [root README](/README.md#-getting-started).*

---

## 🚀 Your First Python Program
### Method 1: Interactive Shell
```python
>>> print("Hello, Python!")
Hello, Python!
```

### Method 2: Script File
1. Create `hello.py`:
   ```python
   print("Hello, Python!")
   ```
2. Run it:
   ```bash
   python hello.py
   ```

---

## 🔄 Python vs. Other Languages
### Example: "Hello World" Comparison
| Language | Code | Lines |
|----------|------|-------|
| **Python** | `print("Hello World")` | 1 |
| **Java** | `public class HelloWorld { public static void main(String[] args) { System.out.println("Hello World"); } }` | 5 |
| **C++** | `#include <iostream> \n int main() { std::cout << "Hello World"; return 0; }` | 3 |

✅ **Python Wins**: Cleaner syntax, fewer lines, no boilerplate!

---

## 🌍 Real-World Scenario: Temperature Converter
Let’s build a simple Celsius-to-Fahrenheit converter:
```python
# Get user input
celsius = float(input("Enter temperature in Celsius: "))

# Convert to Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Display result
print(f"{celsius}°C = {fahrenheit}°F")
```

**Output**:
```
Enter temperature in Celsius: 25
25.0°C = 77.0°F
```

---

## 📝 Basic Input/Output
### Output with `print()`
```python
print("Welcome to Python!")  # Output: Welcome to Python!
```

### Input with `input()`
```python
name = input("What's your name? ")
print(f"Hello, {name}! 👋")
```

**Output**:
```
What's your name? Alice
Hello, Alice! 👋
```

---

---

## ✅ Try It Yourself: 
1. **Modify the temperature converter to accept Fahrenheit and convert to Celsius!**
    ```python
    # Get user input
    celsius = float(input("Enter temperature in Celsius: "))
    
    # Convert to Fahrenheit
    fahrenheit = (celsius * 9/5) + 32
    
    # Display result
    print(f"{celsius}°C = {fahrenheit}°F")
    ```

## 📚 Resources
- **Official Python Documentation**: [docs.python.org](https://docs.python.org/3/)
- **PEP 8 Style Guide**: [Python Code Standards](https://peps.python.org/pep-0008/)
- **Python Community**: [Python.org Community](https://www.python.org/community/)

---

## ➡️ What’s Next?
Ready to explore **Python Data Types**? Head over to [02-data-types-variables](/02-data-types-variables)!
