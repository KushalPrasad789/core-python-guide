# 🐍 Introduction to Python

Welcome to the **Introduction to Python**! This unit covers Python's history, a quick installation guide, and writing your first program. Let’s dive in!

---

## 📜 History of Python
Python was conceived in the late 1980s, and its implementation began in December 1989 by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands. It was designed to be an easy-to-read language that emphasizes readability and simplicity, making it accessible to beginners and powerful for experts.
### 📅 Key Milestones
- **1991**: Created by **Guido van Rossum** to emphasize code readability.
- **2000**: Python 2.0 released (legacy version, now deprecated).
- **2008**: Python 3.0 released (backward-incompatible, current standard).
- **2020**: Python 3.9 introduced faster updates and new syntax features.

```text
```text
📅 Timeline:
1991 🡪 Python 1.0
2000 🡪 Python 2.0
2008 🡪 Python 3.0
2023 🡪 Python 3.11 (Latest)
```

💡 **Fun Fact**: Python is named after the British comedy series *Monty Python*!

---

## 🚀 Getting Started to Program
Before starting to write a program, we need a Python interpreter and a code editor. The Python interpreter is essential for executing Python code, while a code editor provides a user-friendly environment to write and manage your scripts. Popular code editors include Visual Studio Code, PyCharm, and Sublime Text.
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
Python is known for its cleaner syntax and its extensive libraries. Python's standard library is vast and includes modules for various tasks such as web development, data analysis, machine learning, and more. This makes Python a versatile language suitable for many different applications.
### 🌟 Example: "Hello World" Comparison

<table>
   <thead>
      <tr>
         <th>Language</th>
         <th>Code</th>
         <th>Lines</th>
      </tr>
   </thead>
   <tbody>
      <tr>
         <td><strong>Python</strong></td>
         <td><code>print("Hello World")</code></td>
         <td>1</td>
      </tr>
      <tr>
         <td><strong>Java</strong></td>
         <td><code>public class HelloWorld {<br> public static void main(String[] args) {<br> System.out.println("Hello World");<br> }<br> }</code></td>
         <td>5</td>
      </tr>
      <tr>
         <td><strong>C++</strong></td>
         <td><code>#include &lt;iostream&gt;<br> int main() {<br> std::cout &lt;&lt; "Hello World";<br> return 0;<br> }</code></td>
         <td>5</td>
      </tr>
   </tbody>
</table>

✅ **Python Wins**: Cleaner syntax, fewer lines, no boilerplate!

---

## 📝 Basic Input/Output
Input and output are fundamental operations in any programming language. They allow a program to interact with the user or other systems. In Python, these operations are straightforward and easy to use.

### Output with `print()`
The `print()` function is used to display output to the console.
```python
print("Welcome to Python!")  # Output: Welcome to Python!
```

### Input with `input()`
The `input()` function is used to take input from the user. It always returns the input as a string.
```python
name = input("What's your name? ")
print(f"Hello, {name}! 👋")
```

**Example Output**:
```
What's your name? Alice
Hello, Alice! 👋
```

## 🧵 Formatted Strings
Formatted strings in Python allow you to embed expressions inside string literals, using curly braces `{}`. This makes it easy to create strings that include variable values or expressions.

### Using `f-strings`
Introduced in Python 3.6, `f-strings` (formatted string literals) are prefixed with an `f` and use curly braces to embed expressions.
```python
name = "Alice"
age = 30
print(f"Hello, {name}! You are {age} years old.")
```

**Output**:
```
Hello, Alice! You are 30 years old.
```

### Using `str.format()`
The `str.format()` method is another way to format strings. It uses curly braces as placeholders which are replaced by the arguments passed to the method.
```python
name = "Bob"
age = 25
print("Hello, {}! You are {} years old.".format(name, age))
```

**Output**:
```
Hello, Bob! You are 25 years old.
```

### Using `%` Operator
The `%` operator is an older method for string formatting. It uses `%` followed by a format specifier.
```python
name = "Charlie"
age = 22
print("Hello, %s! You are %d years old." % (name, age))
```

**Output**:
```
Hello, Charlie! You are 22 years old.
```

Formatted strings make it easy to create dynamic and readable strings in Python.

---

## 🚨 Common Pitfalls
### 1. **Input Value**
```python
a = input("Enter first number: ")
b = input("Enter second number: ")
print("The sum is:", a + b)  # Error: This concatenates strings, not adds numbers!
```  
**Fix**: Convert types explicitly:  
```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("The sum is:", a + b)
```

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
