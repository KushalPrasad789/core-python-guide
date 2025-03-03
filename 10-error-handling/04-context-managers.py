# Use contextlib to safely read/write files.

import contextlib

@contextlib.contextmanager
def open_file(name, mode):
    try:
        f = open(name, mode)
        yield f
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        try:
            f.close()
        except NameError:
            pass

with open_file('example.txt', 'w') as f:
    f.write('Hello, world!')