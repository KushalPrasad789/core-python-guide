# Combine {"a": 1} and {"b": 2} into {"a": 1, "b": 2}.

# Method 1: Using the update() method
dict1 = {"a": 1}
dict2 = {"b": 2}
dict1.update(dict2)
print(dict1)

# Method 2: Using the ** operator
dict1 = {"a": 1}
dict2 = {"b": 2}
dict3 = {**dict1, **dict2}
print(dict3)

# Method 3: Using the dict() constructor
dict1 = {"a": 1}
dict2 = {"b": 2}
dict3 = dict(dict1, **dict2)
print(dict3)

# Using | operator (Python 3.9+)
dict1 = {"a": 1}
dict2 = {"b": 2}
dict3 = dict1 | dict2
print(dict3)