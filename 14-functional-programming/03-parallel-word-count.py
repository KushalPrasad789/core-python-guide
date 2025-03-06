# Use multiprocessing.Pool to count words in multiple files.

import os
import multiprocessing

# Create sample text files for testing
sample_files = {
    "file1.txt": "Hello world! This is file 1 with some text.",
    "file2.txt": "This is file 2. It contains more words than file 1.",
    "file3.txt": "File 3 has the most words among all files for testing."
}

for filename, content in sample_files.items():
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

print("Sample files created successfully.")


# Function to count words in a single file
def count_words_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            word_count = len(text.split())  # Count words
            return file_path, word_count
    except Exception as e:
        return file_path, f"Error: {e}"

# Function to process multiple files using multiprocessing
def count_words_in_multiple_files(file_paths):
    with multiprocessing.Pool(processes=os.cpu_count()) as pool:
        results = pool.map(count_words_in_file, file_paths)
    return results

if __name__ == "__main__":
    # List of text files
    files = ["file1.txt", "file2.txt", "file3.txt"]

    # Run multiprocessing word count
    results = count_words_in_multiple_files(files)

    # Print results
    for file, count in results:
        print(f"{file}: {count} words")
