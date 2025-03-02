# Use string methods to check if a password has:
# ≥ 8 characters
# At least one uppercase and one digit

password = "Password1"

is_valid = len(password) >= 8 and any(c.isupper() for c in password) and any(c.isdigit() for c in password) # any() returns True if at least one element in the iterable is True.

print(is_valid) # True
