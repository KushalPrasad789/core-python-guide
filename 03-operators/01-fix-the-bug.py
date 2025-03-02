# Why does this return False?  
a = 10  
b = 10.0  
print(a is b)  
# This returns false because the 'is' operator checks if the two variables are the same object, not if they are equal.
# In this case, a and b are not the same object, so the 'is' operator returns False.