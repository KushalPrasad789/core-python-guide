# Replace except: with specific exception handling in:
#    try:  
#        user_input = int(input("Enter a number: "))  
#    except:  
#        print("Error!") 

try:
    user_input = int(input("Enter a number: "))
except ValueError:
    print("Error! Please enter a valid number.")