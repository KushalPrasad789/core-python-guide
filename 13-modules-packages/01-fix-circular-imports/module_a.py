# module_a.py

# ---------------------------------------------------------

# from module_b import function_b

# def function_a():
#     print("Function A")
#     function_b()

# ---------------------------------------------------------

# This is a circular import. module_a imports function_b from module_b, and module_b imports function_a from module_a.
# To fix this, you can move the import statement inside the function definition.

def function_a():
    print("Function A")
    from module_b import function_b  # Local import inside function
    function_b()


# Why This Works?
# The import happens only when the function is called, not at the top of the module.
# This prevents Python from getting stuck in a circular import loop.