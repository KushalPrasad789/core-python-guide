# Combine [1, 2, 3] and [4, 5, 6] into [1,2,3,4,5,6] without using +.
# Hint: Use the extend method.

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)