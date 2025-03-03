# Combine file1.txt and file2.txt into merged.txt

with open('file1.txt', 'r') as file1, open('file2.txt', 'r') as file2:
    content1 = file1.read()
    content2 = file2.read()

with open('merged.txt', 'w') as merged:
    merged.write(content1 + "\n" + content2)
