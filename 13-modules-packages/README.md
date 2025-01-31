# 📦 Python Modules & Packages: Organize, Share, and Reuse Code

Learn to structure projects, create reusable packages, and avoid common import pitfalls.  

---

## 🧩 Modules vs. Packages Cheat Sheet  
| Feature | Modules | Packages |  
|---------|---------|----------|  
| **Definition** | Single `.py` file | Directory with `__init__.py` |  
| **Import Syntax** | `import my_module` | `from my_package import module` |  
| **Namespace** | Global or local | Hierarchical (e.g., `package.subpackage`) |  
| **Use Case** | Small utilities | Large projects, libraries |  

---

## 🚨 Common Pitfalls & Fixes  
### 1. **Circular Imports**  
```python  
# module_a.py  
import module_b  # module_b imports module_a → Error!  
```  
✅ **Fix**: Refactor code or use local imports.  

### 2. **Shadowing Standard Modules**  
```python  
# math.py (custom module)  
import math  # Imports your math.py, not the standard library!  
```  
✅ **Fix**: Avoid naming modules after built-in modules.  

### 3. **Missing `__init__.py`**  
```text
my_package/  
    module.py  # Not recognized as a package without __init__.py  
```  
✅ **Fix**: Add empty `__init__.py` (or use namespace packages).  

---

## 🔍 Core Concepts  
### **Absolute vs. Relative Imports**  
| Type | Syntax | Use Case |  
|------|--------|----------|  
| Absolute | `from package import module` | Clarity, avoids ambiguity |  
| Relative | `from .subpackage import module` | Intra-package imports |  

### **Namespace Packages (PEP 420)**  
Split a package across multiple directories without `__init__.py`:  
```text
project/  
    dir1/  
        my_namespace/  
            module1.py  
    dir2/  
        my_namespace/  
            module2.py  
```  
```python  
# Both modules are accessible under my_namespace  
from my_namespace import module1, module2  
```  

---

## 🌍 Real-World Scenarios  
### 1. **CLI Tool as a Package**  
```text
my_cli/  
    __init__.py  
    cli.py  
    utils/  
        __init__.py  
        helpers.py  
```  
```python  
# cli.py  
def main():  
    print("Running CLI...")  

if __name__ == "__main__":  
    main()  
```  

### 2. **Web API Structure**  
```text
my_api/  
    __init__.py  
    routes/  
        __init__.py  
        users.py  
    models/  
        __init__.py  
        user.py  
    utils/  
        __init__.py  
        auth.py  
```  

### 3. **Publishing to PyPI**  
1. Create `pyproject.toml`:  
```toml  
[build-system]  
requires = ["setuptools>=64.0"]  
build-backend = "setuptools.build_meta"  

[project]  
name = "my_package"  
version = "0.1.0"  
```  
2. Build and upload:  
```bash  
python -m build  
twine upload dist/*  
```  

---

## 💡 Advanced Features  
### **Entry Points for CLI Tools**  
```toml  
# pyproject.toml  
[project.scripts]  
my-cli = "my_package.cli:main"  
```  
Run as: `my-cli`  

### **Type Hints in Modules**  
```python  
# math_utils.py  
from typing import Union  

def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:  
    return a + b  
```  

### **Security Best Practices**  
- Avoid wildcard imports: `from module import *`  
- Use `__all__` to limit exposed names:  
```python  
__all__ = ["public_function"]  # Controls `from module import *`  
```  

---

## ✅ Try It Yourself!  
1. **Fix Circular Imports**:  
   Refactor a project where `module_a.py` imports `module_b.py` and vice versa.  

2. **Create a Namespace Package**:  
   Split a package across two directories and import modules from both.  

3. **Convert Script to Package**:  
   Transform a standalone script into a package with `setup.py`/`pyproject.toml`.  

---

## 📚 Resources  
- **Python Docs**: [Modules](https://docs.python.org/3/tutorial/modules.html)  
- **Packaging Guide**: [PyPA](https://packaging.python.org/en/latest/)  

---

## ➡️ What’s Next?  
Ready to embrace functional programming? Head over to [14-functional-programming](/14-functional-programming)!  
