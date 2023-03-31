# Commodity Trader Game
# Buy/Sell Different Resources to Amass a Fortune
# Travel to Different Cities with Different Prices

import City
import Resource
import Player
import Engine


player = Player.Player()

engine = Engine.Engine()
engine.main_loop()

city1 = City.City("New Startland", 3, 3)

# Think of a good way to initialize all resources at the start of running the program

# Adding test resources for the city to sell
wheat = Resource.Resource("Wheat", 5, 20, 0, 0)
stone = Resource.Resource("Stone", 5, 20, 0, 0)
wood = Resource.Resource("Wood", 5, 20, 0, 0)
city1.add_resource_sell(wheat)
city1.add_resource_sell(stone)
city1.add_resource_sell(wood)

# Adding test resources for the city to buy
rice = Resource.Resource("Wheat", 0, 0, 5, 20)          # Name is changed for testing purposes
iron = Resource.Resource("Iron", 0, 0, 5, 20)
cotton = Resource.Resource("Cotton", 0, 0, 5, 20)
city1.add_resource_buy(rice)
city1.add_resource_buy(iron)
city1.add_resource_buy(cotton)

# Testing buying items as player
# player.buy_item(city1.inventory_selling.inventory[0])
# player.buy_item(city1.inventory_selling.inventory[1])
# player.buy_item(city1.inventory_selling.inventory[0])
# player.buy_item(city1.inventory_selling.inventory[2])
# player.buy_item(city1.inventory_selling.inventory[0])


