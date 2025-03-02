# Turn [["name", "Alice"], ["age", 25]] into {"name": "Alice", "age": 25}.

# Given a list of lists, where each list contains two items, turn it into a dictionary.
nested_list = [["name", "Alice"], ["age", 25]]
result_dict = dict(nested_list)
print(result_dict)