# Write a decorator to log how long a function takes to run.

import time

def execution_time_logger(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.4f} seconds to execute.")
        return result
    return wrapper

@execution_time_logger
def test_function():
    for _ in range(1000000):
        pass

test_function()