# Commodity Trader Game
# Buy/Sell Different Resources to Amass a Fortune
# Travel to Different Cities with Different Prices

import Inventory

player_inventory = Inventory.Inventory(5)

player_inventory.print_inventory()

print()

player_inventory.add_item("Wheat")
player_inventory.add_item("Stone")
player_inventory.add_item("Stone")
player_inventory.add_item("Stone")
player_inventory.add_item("Stone")
player_inventory.add_item("Wood")

player_inventory.remove_item("Wood")

player_inventory.print_inventory()


# Dictionary For Item:Value
resources = {
    "Wheat": 5,
    "Stone": 10
}

print()

print(resources)
