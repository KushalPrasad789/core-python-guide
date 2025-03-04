# Modify the Inventory class to prevent shared items across instances.

class Inventory:
	def __init__(self):
		self.items = []

	def add_item(self, item):
		self.items.append(item)

	def get_items(self):
		return self.items

# Example usage:
inventory1 = Inventory()
inventory1.add_item("apple")
print(inventory1.get_items())  # Output: ['apple']

inventory2 = Inventory()
inventory2.add_item("banana")
print(inventory2.get_items())  # Output: ['banana']

