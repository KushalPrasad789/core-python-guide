# Validate passwords using:
# •	≥ 8 characters
# •	At least 1 uppercase, 1 digit, and 1 special character.

while True:
    password = input("Enter a password to check: ")

    if len(password) < 8:
        print("Password must be at least 8 characters long.")
    elif not any(char.isupper() for char in password):
        print("Password must contain at least one uppercase letter.")
    elif not any(char.isdigit() for char in password):
        print("Password must contain at least one digit.")
    elif not any(char in "!@#$%^&*(),.?\":{}|<>" for char in password):
        print("Password must contain at least one special character.")
    else:
        print("Password is strong.")
        break
