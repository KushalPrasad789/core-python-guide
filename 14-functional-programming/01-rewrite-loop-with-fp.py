# Convert [x*2 for x in data if x > 0] using map/filter.

data = [1, -2, 3, -4, 5]

result = list(map(lambda x: x * 2, filter(lambda x: x > 0, data)))
print(result)