# Debug this code to make the counter work:
#    def counter():  
#        count = 0  
#        return lambda: count += 1  # Error! 

def counter():
    count = 0
    return lambda: count + 1

# Test the function
count = counter()
print(count())
