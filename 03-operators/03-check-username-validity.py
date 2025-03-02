# Use and/or to validate:
# •	Length >= 6
# •	Contains letters and numbers.

username = input("Enter username: ")

if len(username) >= 6 and username.isalnum():
    print("Valid username")
else:
    print("Invalid username")
