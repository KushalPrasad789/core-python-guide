# 🚀 Advanced Python Concepts: Generators, Regex, Concurrency & More

Master Python’s advanced features to build high-performance, scalable, and secure applications.  

---

## 🧩 Advanced Concepts Cheat Sheet  
| Feature | Syntax | Use Case |  
|---------|--------|----------|  
| **Generator** | `yield` | Lazy data streams |  
| **Regex** | `re.compile(r"\d+")` | Pattern matching |  
| **Async/Await** | `async def`, `await` | Non-blocking I/O |  
| **Metaclass** | `class Meta(type):` | Dynamic class creation |  
| **Type Hints** | `def func() -> int:` | Static code analysis |  

---

## 🚨 Common Pitfalls & Fixes  
### 1. **Generator Exhaustion**  
```python  
data = (x for x in range(3))  
print(list(data))  # [0, 1, 2]  
print(list(data))  # [] (Already exhausted!)  
```  
✅ **Fix**: Re-initialize generators or use `itertools.tee`.  

### 2. **Catastrophic Backtracking (Regex ReDoS)**  
```python  
# Dangerous pattern: Exponential backtracking  
re.match(r"(a+)+b", "aaaaaaaaac")  # Extremely slow!  
```  
✅ **Fix**: Use atomic groups or simplify patterns:  
```python  
re.match(r"(?>a+)+b", "aaaaaaaaac")  # Fails quickly  
```  

### 3. **Thread Safety Issues**  
```python  
from threading import Thread  

counter = 0  
def increment():  
    global counter  
    for _ in range(1000):  
        counter += 1  # Race condition!  

threads = [Thread(target=increment) for _ in range(10)]  
[t.start() for t in threads]  
[t.join() for t in threads]  
print(counter)  # Likely < 10000!  
```  
✅ **Fix**: Use `threading.Lock()` or `multiprocessing`.  

---

## 🔍 Core Concepts  
### **Generators vs. Lists**  
| Generators | Lists |  
|------------|-------|  
| Lazy evaluation | Eager evaluation |  
| Memory-efficient | Memory-heavy |  
| Single-use | Reusable |  

### **Concurrency Performance Comparison: Threads vs. Processes vs. Async**  
| Approach | Use Case | Pros | Cons |  Library |  
|----------|----------|------|------|-----------| 
| **Threads** | I/O-bound tasks | Lightweight | GIL-bound | `threading` |
| **Processes** | CPU-bound tasks | Parallelism | High overhead | `multiprocessing` |
| **Async** | High I/O concurrency | Scalable | Complex setup | `asyncio` |

### **Regex Syntax Cheat Sheet**  
| Pattern | Matches | Example |  
|---------|---------|---------|  
| `\d` | Digit | `"A1"` → `"1"` |  
| `\w` | Word character | `"user_1"` → `"user_1"` |  
| `^` | Start of string | `^Hello` → `"Hello World"` |  
| `$` | End of string | `World$` → `"Hello World"` |  
| `(?:...)` | Non-capturing group | `(?:ab)+` → `"abab"` |  


### **Debugging Generators with `inspect`**  
```python  
import inspect  

gen = (x for x in range(3))  
print(inspect.getgeneratorstate(gen))  # GEN_CREATED  

next(gen)  
print(inspect.getgeneratorstate(gen))  # GEN_SUSPENDED  
```  

---

## 🌍 Real-World Scenarios  
### 1. **Data Validation with `pydantic`**  
```python  
from pydantic import BaseModel, ValidationError  

class User(BaseModel):  
    name: str  
    age: int  

try:  
    user = User(name="Alice", age="twenty")  # ValidationError  
except ValidationError as e:  
    print(e.json())  
```  

### 2. **Async Web Scraper with `aiohttp`**  
```python  
import aiohttp  
import asyncio  

async def fetch(url):  
    async with aiohttp.ClientSession() as session:  
        async with session.get(url) as response:  
            return await response.text()  

async def main():  
    html = await fetch("https://example.com")  
    print(html[:100])  

asyncio.run(main())  
```  

### 3. **Async Web Server with `asyncio`**  
```python  
from aiohttp import web  

async def handle(request):  
    return web.Response(text="Hello, async world!")  

app = web.Application()  
app.add_routes([web.get("/", handle)])  

if __name__ == "__main__":  
    web.run_app(app)  
```  

### 4. **Regex for Log Analysis**  
```python  
import re  

log = "ERROR: [2023-09-20] User 'admin' failed login"  
pattern = r"ERROR: \[(\d{4}-\d{2}-\d{2})\] User '(\w+)' failed login"  
match = re.search(pattern, log)  
if match:  
    date, user = match.groups()  
    print(f"Alert: {user} failed on {date}")  
```  

### 5. **Data Streaming with Generators**  
```python  
def read_large_file(file_path):  
    with open(file_path) as f:  
        for line in f:  
            yield line.strip()  

# Process 1GB file without loading it into memory  
for line in read_large_file("data.csv"):  
    process(line)  
```  

### 6. **Metaclass for Validation**  
```python  
class ValidatorMeta(type):  
    def __new__(cls, name, bases, dct):  
        if "validate" not in dct:  
            raise TypeError("Missing validate() method")  
        return super().__new__(cls, name, bases, dct)  

class User(metaclass=ValidatorMeta):  
    def validate(self):  
        return len(self.name) > 0  
```  

---

## 💡 Advanced Features  
### **Metaclasses for Dynamic Classes**  
```python  
class SingletonMeta(type):  
    _instances = {}  
    def __call__(cls, *args, **kwargs):  
        if cls not in cls._instances:  
            cls._instances[cls] = super().__call__(*args, **kwargs)  
        return cls._instances[cls]  

class Logger(metaclass=SingletonMeta):  
    pass  

logger1 = Logger()  
logger2 = Logger()  
print(logger1 is logger2)  # True  
```  

### **Memory Profiling**  
```python  
import tracemalloc  

tracemalloc.start()  
data = [x for x in range(10**6)]  
snapshot = tracemalloc.take_snapshot()  
for stat in snapshot.statistics("lineno")[:3]:  
    print(stat)  
```  

### **Type Hint Generics**  
```python  
from typing import Generic, TypeVar  

T = TypeVar("T")  

class Box(Generic[T]):  
    def __init__(self, item: T):  
        self.item = item  

box = Box[int](10)  
```  

---

## ✅ Try It Yourself!  
1. **Prevent ReDoS**:  
   Optimize the regex `r"(\d+|\w+)+$"` to avoid catastrophic backtracking.  

2. **Thread-Safe Counter**:  
   Fix the thread example to ensure `counter` reaches 10000 using locks.  

3. **Generator Debugging**:  
   Use `inspect` to track the state of a generator iterating over a large file.

4. **Async File Downloader**:  
    Use aiohttp to download multiple URLs concurrently.  

---

## 📚 Resources  
- **Regex Security**: [OWASP ReDoS Guide](https://owasp.org/www-community/attacks/Regular_expression_Denial_of_Service_-_ReDoS)  
- **Pydantic Docs**: [Data Validation Made Easy](https://docs.pydantic.dev/)  
- **Regex Guide**: [Regular-Expressions.info](https://www.regular-expressions.info/)  
- **Asyncio Docs**: [Python Docs](https://docs.python.org/3/library/asyncio.html)  


---

## ➡️ What’s Next?  
Ready to work with **APIs & Data**? Head over to [16-apis-data](/16-apis-data)!  
