# Commodity Trader Game
# Buy/Sell Different Resources to Amass a Fortune
# Travel to Different Cities with Different Prices

import City
import Resource

city1 = City.City("New Startland", 3)

wheat = Resource.Resource("Wheat", 5, 20, 1, 5)
stone = Resource.Resource("Stone", 5, 20, 1, 5)
wood = Resource.Resource("Wood", 5, 20, 1, 5)
iron = Resource.Resource("Iron", 5, 20, 1, 5)

city1.add_resource(wheat)
city1.add_resource(stone)
city1.add_resource(wood)
city1.add_resource(iron)        # FIXED  Allows adding past maximum inventory size

city1.print_resources()         # Might not be used later

print()
for x in range(100):
    print("Day: {}".format(x))
    city1.new_day()
    city1.print_inventory_sell()
    print()

