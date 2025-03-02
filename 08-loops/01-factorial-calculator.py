# Use a loop to compute 5! = 5*4*3*2*1

num = 5
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"The factorial of {num} is {factorial}")
