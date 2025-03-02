# Convert (("name", "Alice"), ("age", 25)) into {"name": "Alice", "age": 25}.

# The tuple contains a list of key-value pairs.
# We can convert this into a dictionary by iterating over the tuple and adding the key-value pairs to a dictionary.
# We can also use a dictionary comprehension to achieve this.

tuples = (("name", "Alice"), ("age", 25))
# Using a dictionary comprehension
# For each tuple, the first element becomes the key and the second element becomes the value
dictionary = {key: value for key, value in tuples}
print(dictionary)

# Using a loop
dictionary = {}
for key, value in tuples:
    dictionary[key] = value
print(dictionary)
