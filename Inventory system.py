# Inventory System
inventory = ["Flour","Sugar","Salt"]
items = input("Add an item to shop: ")
if items in inventory:
    print("Item is already availlable.")
    print("Availlable items:",inventory)
else: inventory.append(items)
print("Item added Successfully!")
print("Currently availlable items:",inventory)
