# Count ERROR entries in a log file named 'logfile.txt'

error_count = 0

with open('logfile.txt', 'r') as log_file:
    for line in log_file:
        if "ERROR" in line:
            error_count += 1

print("Total ERROR entries:", error_count)
