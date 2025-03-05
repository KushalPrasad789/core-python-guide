3. **Convert Script to Package**:  
   Transform a standalone script into a package with `setup.py`/`pyproject.toml`.


```
03-convert-script-package/  # Root project directory
│── my_package/          # Package directory
│   ├── __init__.py      # Makes this a package
│   ├── my_script.py     # The original script moved inside the package
│── setup.py             # Packaging metadata (Setuptools-based)
│── pyproject.toml       # Modern metadata (PEP 517-based)
│── README.md            # Project description
│── requirements.txt     # Dependencies (optional)
│── LICENSE              # License file (optional)
```