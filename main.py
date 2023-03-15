# Commodity Trader Game
# Buy/Sell Different Resources to Amass a Fortune
# Travel to Different Cities with Different Prices

import City
import Resource

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
rice = Resource.Resource("Rice", 0, 0, 5, 20)
iron = Resource.Resource("Iron", 0, 0, 5, 20)
cotton = Resource.Resource("Cotton", 0, 0, 5, 20)

city1.add_resource_buy(rice)
city1.add_resource_buy(iron)
city1.add_resource_buy(cotton)

city1.print_resources()         # Might not be used later

print()
for x in range(100):
    print("Day: {}".format(x))
    city1.new_day()
    city1.print_inventory_buy()
    print()

