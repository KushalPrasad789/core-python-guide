# Create InvalidEmailError for invalid email formats.

def validate_email(email):
    if "@" not in email or "." not in email.split("@")[-1]:
        raise ValueError(f"Invalid email format: {email}")
    return True

# Test the function
try:
    validate_email("valid.email@example.com")
    print("Email is valid.")
except ValueError as e:
    print(e)

try:
    validate_email("invalid-email")
except ValueError as e:
    print(e)
