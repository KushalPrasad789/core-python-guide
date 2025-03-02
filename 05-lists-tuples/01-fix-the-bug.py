# Why does this fail? Fix it!  
config = ("localhost", 8080)  
# config[1] = 8000  # Throws an error because the tuple is immutable
config = ("localhost", 8000)  # This is the correct way to change the value of a tuple
print(config)

# You can also convert the tuple to a list, change the value and then convert it back to a tuple
config = list(config)
config[1] = 8080
config = tuple(config)
print(config)
