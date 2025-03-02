# Use isinstance() to validate input types.
def add(a, b):  
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):  
        return a + b  
    raise TypeError("Numbers only!")  # Skip if unfamilier to it for now

print(add(10, 20))