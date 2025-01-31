# 🧠 Python Functional Programming: Write Clean, Efficient Code

Leverage functional programming (FP) concepts like immutability, higher-order functions, and decorators to build robust pipelines.  

---

## 🧩 FP Cheat Sheet  
| Tool | Syntax | Purpose |  
|------|--------|---------|  
| **`map()`** | `map(func, iterable)` | Apply function to all items |  
| **`filter()`** | `filter(func, iterable)` | Filter items by condition |  
| **`reduce()`** | `reduce(func, iterable)` | Aggregate values (from `functools`) |  
| **`lambda`** | `lambda x: x*2` | Anonymous single-expression functions |  
| **`@lru_cache`** | `functools.lru_cache` | Memoization for expensive calls |  
| **`partial`** | `functools.partial` | Pre-fill function arguments |  

---

## 🚨 Common Pitfalls & Fixes  
### 1. **Overusing Lambda for Complex Logic**  
```python  
# Hard to read!  
sorted_data = sorted(data, key=lambda x: (x[1], -x[0]))  
```  
✅ **Fix**: Use named functions or `operator` module:  
```python  
from operator import itemgetter  
sorted_data = sorted(data, key=itemgetter(1))  
```  

### 2. **Ignoring Immutability**  
```python  
def process(items):  
    items.append("new")  # Modifies input!  
```  
✅ **Fix**: Return new collections:  
```python  
def process(items):  
    return [*items, "new"]  
```  

### 3. **Lazy Evaluation Surprises**  
```python  
squares = map(lambda x: x**2, data)  
print(list(squares))  # Exhausts the iterator!  
```  

---

## 🔍 Core Concepts  
### **FP vs. Imperative Performance**  
```python  
import timeit  

# Imperative approach  
def sum_squares_imperative(n):  
    total = 0  
    for i in range(n):  
        total += i ** 2  
    return total  

# FP approach  
def sum_squares_fp(n):  
    return sum(map(lambda x: x**2, range(n)))  

print(timeit.timeit(lambda: sum_squares_imperative(1000)))  # ~0.06s  
print(timeit.timeit(lambda: sum_squares_fp(1000)))          # ~0.04s  
```  

### **Recursive Decorators**  
```python  
def retry(max_attempts=3):  
    def decorator(func):  
        def wrapper(*args, **kwargs):  
            attempts = 0  
            while attempts < max_attempts:  
                try:  
                    return func(*args, **kwargs)  
                except Exception as e:  
                    attempts += 1  
            raise RuntimeError("Max retries exceeded")  
        return wrapper  
    return decorator  

@retry(max_attempts=2)  
def fetch_data(url):  
    # Simulate API call  
    if "example.com" not in url:  
        raise ConnectionError  
    return "Data"  

fetch_data("https://test.com")  # Retries twice → RuntimeError  
```  

---

## 🌍 Real-World Scenarios  
### 1. **Data Transformation Pipeline**  
```python  
from functools import reduce  

data = [1, 2, 3, 4, 5]  
pipeline = (  
    data  
    |> (lambda x: filter(lambda n: n % 2 == 0, x))  
    |> (lambda x: map(lambda n: n * 2, x))  
    |> (lambda x: reduce(lambda a, b: a + b, x))  
)  
print(pipeline)  # (2*2 + 4*2) = 12  
```  

### 2. **Parallel Processing with `multiprocessing`**  
```python  
from multiprocessing import Pool  

def square(n):  
    return n ** 2  

with Pool(4) as p:  
    results = p.map(square, range(10))  # [0, 1, 4, 9, ..., 81]  
```  

### 3. **Caching Expensive Calls**  
```python  
from functools import lru_cache  

@lru_cache(maxsize=128)  
def fibonacci(n):  
    if n <= 1:  
        return n  
    return fibonacci(n-1) + fibonacci(n-2)  

print(fibonacci(100))  # Computed efficiently!  
```  

---

## 💡 Advanced Features  
### **Third-Party FP Libraries**  
#### **`toolz` for Function Composition**  
```python  
from toolz import compose  

clean = compose(str.strip, str.lower)  
print(clean("  Hello "))  # "hello"  
```  

#### **`fn.py` for Pattern Matching**  
```python  
from fn import _  

# Filter even numbers greater than 10  
filter(_ % 2 == 0 and _ > 10, [5, 8, 12, 15])  # [12]  
```  

### **Partial Function Application**  
```python  
from functools import partial  

def power(base, exponent):  
    return base ** exponent  

square = partial(power, exponent=2)  
print(square(5))  # 25  
```  

---

## ✅ Try It Yourself!  
1. **Rewrite Loop with FP**:  
   Convert `[x*2 for x in data if x > 0]` using `map`/`filter`.  

2. **Memoized Factorial**:  
   Use `@lru_cache` to optimize a recursive factorial function.  

3. **Parallel Word Count**:  
   Use `multiprocessing.Pool` to count words in multiple files.  

---

## 📚 Resources  
- **Functional HOWTO**: [Python Docs](https://docs.python.org/3/howto/functional.html)  
- **`toolz`**: [Toolz Documentation](https://toolz.readthedocs.io/)  

---

## ➡️ What’s Next?  
Ready for **Advanced Python Concepts**? Head over to [15-advanced-concepts](/15-advanced-concepts)!  
