def create_inventory(items):
    inventory = {}
    for item in list(set(items)):               #making a list of unique items
        inventory[item] = items.count(item)
    return inventory


def add_items(inventory, items):
    new_items = create_inventory(items)         #seeing the inventory of the new list
    for item in new_items:
        if item in inventory:                   #checking if we have the same items in both list
            inventory[item] = inventory[item] + items.count(item)       #if yes, add them together
            continue
        inventory[item] = items.count(item)     #if not, add normally
    return inventory


def decrement_items(inventory, items):
    new_items = create_inventory(items)
    for item in new_items:                      #the same thing but now we don't need to see if the items in the new list are in the inventory
        testing = inventory[item] - items.count(item)       #but we have to check if the decrement does not go below zero
        if testing >= 0:
            inventory[item] = testing
            continue
        inventory[item] = 0
    return inventory


def remove_item(inventory, item):
    inventory.pop(item, inventory)
    return inventory


def list_inventory(inventory):
    list_of_items = []
    for item in inventory:
        if inventory[item] != 0:
            list_of_items.append((item, inventory[item]))
    return list_of_items
