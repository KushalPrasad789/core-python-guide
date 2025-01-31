# 📁 Python File Handling: Read, Write, and Manage Files Like a Pro

Master file I/O operations, work with different file types, and handle large datasets efficiently.  

---

## 🧩 File Modes Cheat Sheet  
| Mode | Description |  
|------|-------------|  
| `r` | Read (text, default) |  
| `w` | Write (creates/truncates) |  
| `a` | Append |  
| `x` | Exclusive creation |  
| `rb`/`wb` | Read/write (binary) |  
| `r+`/`w+` | Read+write |  

---

## 🚨 Common Pitfalls & Fixes  
### 1. **Resource Leaks**  
```python  
file = open("data.txt")  # Risk of not closing!  
```  
✅ **Fix**: Use context managers:  
```python  
with open("data.txt") as file:  
    ...  
```  

### 2. **Encoding Issues**  
```python  
# Fails on non-UTF-8 files  
with open("data.txt", "r") as f:  
    ...  
```  
✅ **Fix**: Specify encoding:  
```python  
with open("data.txt", "r", encoding="latin-1") as f:  
    ...  
```  

### 3. **Accidental File Overwrite**  
```python  
with open("data.txt", "w") as f:  # Truncates existing file!  
    ...  
```  
✅ **Fix**: Use `"a"` (append) or check existence first with `pathlib`.  

---

## 🔍 Core Operations  
### **Modern Path Handling with `pathlib`**  
```python  
from pathlib import Path  

# Platform-agnostic paths  
file_path = Path("data") / "report.csv"  
if file_path.exists():  
    content = file_path.read_text()  
```  

### **Reading Large Files in Chunks**  
```python  
with open("large.log", "r") as f:  
    while chunk := f.read(4096):  # Read 4KB chunks  
        process(chunk)  
```  

### **Binary File Operations**  
```python  
# Copy image  
with open("input.jpg", "rb") as src, open("copy.jpg", "wb") as dest:  
    dest.write(src.read())  
```  

---

## 🌍 Real-World Scenarios  
### 1. **CSV/JSON Handling**  
```python  
import csv  
import json  

# CSV to JSON  
with open("data.csv", "r") as csv_file:  
    csv_reader = csv.DictReader(csv_file)  
    data = list(csv_reader)  

with open("data.json", "w") as json_file:  
    json.dump(data, json_file, indent=2)  
```  

### 2. **Rotating Log Files**  
```python  
import logging  
from logging.handlers import RotatingFileHandler  

logger = logging.getLogger(__name__)  
handler = RotatingFileHandler("app.log", maxBytes=1e6, backupCount=3)  # 1MB per file  
logger.addHandler(handler)  
```  

### 3. **ZIP File Extraction**  
```python  
import zipfile  

with zipfile.ZipFile("archive.zip", "r") as zip_ref:  
    zip_ref.extractall("extracted/")  
```  

---

## 💡 Advanced Features  
### **Temporary Files**  
```python  
import tempfile  

with tempfile.NamedTemporaryFile(delete=False) as tmp:  
    tmp.write(b"Temporary data")  
    tmp_path = tmp.name  # Access later  
```  

### **Memory-Mapped Files**  
```python  
import mmap  

with open("large.bin", "rb") as f:  
    with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as mm:  
        print(mm[:10])  # First 10 bytes  
```  

### **File System Operations**  
```python  
import shutil  

# Copy directory  
shutil.copytree("src/", "backup/")  

# Delete directory  
shutil.rmtree("temp/")  
```  

---

## ✅ Try It Yourself!  
1. **Merge Two Files**:  
   Combine `file1.txt` and `file2.txt` into `merged.txt`.  

2. **Log Analyzer**:  
   Count ERROR entries in a log file.  

3. **Directory Size Calculator**:  
   Use `os.walk` to compute total size of a folder.  

---

## 📚 Resources  
- **Python Docs**: [File Objects](https://docs.python.org/3/glossary.html#term-file-object)  
- **Real Python**: [Working With Files](https://realpython.com/working-with-files-in-python/)  

---

## ➡️ What’s Next?  
Ready to master **Object-Oriented Programming**? Head over to [12-object-oriented-programming](/12-object-oriented-programming)!  
