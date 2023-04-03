stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'ring': 1, 'apple': 12,}

def displayInventory(inventory):
    # your code goes here

    #total_inventory_items = 0
    # print('Inventory:')
    # for key,value in inventory.items():
    #     print(value, key)
    #     total_inventory_items += value
    # print('Total number of items:', total_inventory_items)

    #The following code is my original try before watching the video. Updated post video to pass in "inventory" 
    #not "stuff". This one isn't as clean but it does sort the inventory.  
    count = 0
    for key in inventory:
        if inventory[key] > 0:
            count = count + inventory[key]
    lst = list(inventory.keys())
    lst.sort()
    print("Inventory:")
    for key in lst:
        print(inventory[key], key)
    print("Total number of items:", count)

if __name__ == "__main__":
    displayInventory(stuff)
