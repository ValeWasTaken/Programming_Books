# Python 3.4

inventory = {
    'rope': 1,
    'torch': 6,
    'gold coin': 42,
    'dagger': 1,
    'arrow': 12
    }
def display_inventory():
    total_items = 0
    for item in inventory:
        print('{0}: {1}'.format(inventory[item], item))
        total_items += inventory[item]
    print('Total amount of items: {0}'.format(total_items))
display_inventory()
