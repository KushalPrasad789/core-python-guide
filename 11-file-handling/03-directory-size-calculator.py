import os

def get_folder_size(folder):
    total_size = 0
    # os.walk traverses through all directories and files in the given folder
    for dirpath, dirnames, filenames in os.walk(folder):
        for file in filenames:
            file_path = os.path.join(dirpath, file)
            # If it's not a symbolic link, add its size to the total
            if not os.path.islink(file_path):
                total_size += os.path.getsize(file_path)
    return total_size

# Replace 'path/to/folder' with the folder you want to calculate the size of.
folder_path = 'path/to/folder'
size = get_folder_size(folder_path)
print(f"Total size of '{folder_path}' is {size} bytes.")
