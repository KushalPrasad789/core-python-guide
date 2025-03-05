2. **Create a Namespace Package**:  
   Split a package across two directories and import modules from both. 

```
02-create-namespace-package/
│── main.py
│── mypackage/   # A package containing dir1 and dir2
│   ├── __init__.py
│   ├── dir1/
│   │   ├── __init__.py
│   │   ├── module_a.py
│   ├── dir2/
│   │   ├── __init__.py
│   │   ├── module_b.py
```