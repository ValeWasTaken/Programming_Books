# Python 3.4

inventory = {
    'rope': 1,
    'torch': 6,
    'gold coin': 42,
    'dagger': 1,
    'arrow': 12
    }
def display_inventory():
    for item in inventory:
        print('{0}: {1}'.format(inventory[item], item))
display_inventory()
