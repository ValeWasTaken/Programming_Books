# Python 3.4
inventory = {
    'rope': 1,
    'gold coin': 42,
    }
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

for item in dragon_loot: inventory[item] = inventory.get(item, 0) + 1

def display_inventory():
    total_items = 0
    for item in inventory:
        print('{0}: {1}'.format(inventory[item], item))
        total_items += inventory[item]
    print('Total amount of items: {0}'.format(total_items))     
display_inventory()
