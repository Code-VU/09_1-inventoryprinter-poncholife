stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'ring': 1, 'apple': 12}

def displayInventory(inventory):
    print('Inventory:')
    total_items_in_inventory = 0
    for key in inventory:
        total_items_in_inventory += inventory[key]
        print(inventory[key], key)
    print(f'Total number of items: {total_items_in_inventory}')


if __name__ == "__main__":
    displayInventory(stuff)