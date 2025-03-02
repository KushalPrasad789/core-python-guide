# 1. Modify the temperature converter to accept Fahrenheit and convert to Celsius!  

# Get user input
fahrenheit = float(input("Enter temperature in Celsius: "))

# Convert to Fahrenheit
celsius = (fahrenheit - 32) * 5/9

# Display result
print(f"{fahrenheit}°F = {celsius:.2f}°C")