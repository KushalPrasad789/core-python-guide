# Convert ["10", "20", "30"] to a list of integers.

list_of_strings = ["10", "20", "30"]

# list_of_integers = [int(i) for i in list_of_strings] # List comprehension
# list_of_integers = list(map(int, list_of_strings)) # Using map function

list_of_integers = []
for i in list_of_strings:
    list_of_integers.append(int(i))

print(list_of_integers) # Output: [10, 20, 30]