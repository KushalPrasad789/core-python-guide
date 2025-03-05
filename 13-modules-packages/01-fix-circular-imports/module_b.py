# module_b.py

# ---------------------------------------------------------

# from module_a import function_a

# def function_b():
#     print("Function B")
#     function_a()

# ---------------------------------------------------------

# This is a circular import. module_a imports function_b from module_b, and module_b imports function_a from module_a.
# To fix this, you can move the import statement inside the function definition.

def function_b():
    print("Function B")
    from module_a import function_a  # Local import inside function
    function_a()

# Why This Works?
# The import happens only when the function is called, not at the top of the module.
# This prevents Python from getting stuck in a circular import loop.