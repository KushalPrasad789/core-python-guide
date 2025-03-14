# Implement a function to find an item in a sorted list using recursion.

def binary_search_recursive(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search_recursive(data, target, low, mid - 1)
        else:
            return binary_search_recursive(data, target, mid + 1, high)
        
data = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 29, 31, 33, 36, 39, 40]
target = 25
low = 0
high = len(data) - 1
print(binary_search_recursive(data, target, low, high))
# Output: True
