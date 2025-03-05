import sys
import os

# Get absolute paths of directories (Ensure correct paths)
dir1_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "dir1"))
dir2_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "dir2"))

# Print paths for debugging
print("dir1_path:", dir1_path)
print("dir2_path:", dir2_path)

# Add directories to sys.path
sys.path.extend([dir1_path, dir2_path])

# Print sys.path to confirm directories are included
print("sys.path:", sys.path)

# Import after modifying sys.path
try:
    from module_a import function_a
    from module_b import function_b
except ModuleNotFoundError as e:
    print("Import Error:", e)

function_a()
function_b()
