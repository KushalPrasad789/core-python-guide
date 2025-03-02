# Simplify using nested if:
# if user.is_active:  
#     if user.has_subscription:  
#         print("Access granted") 

# This is an OOP concept which we will cover later
# Focus only ont the conditional statement if
class User:
    def __init__(self, is_active, has_subscription):
        self.is_active = is_active
        self.has_subscription = has_subscription

# Create a user instance
user = User(is_active=True, has_subscription=True)


# Simplified using a single if statement:
if user.is_active and user.has_subscription: # Foucs here only
    print("Access granted")