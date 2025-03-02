# Convert "name,age,email\nAlice,25,alice@mail.com" into a list of dictionaries.

csv_string = "name,age,email\nAlice,25,alice@mail.com"
lines = csv_string.split("\n")
keys = lines[0].split(",")
data = []
for line in lines[1:]:
    values = line.split(",")
    data.append(dict(zip(keys, values)))

print(data)

