# Commodity Trader Game
# Buy/Sell Different Resources to Amass a Fortune
# Travel to Different Cities with Different Prices

import City
import Resource

city1 = City.City("New Startland", 3)

wheat = Resource.Resource("Wheat", 5, 10, 1, 5)
stone = Resource.Resource("Stone", 5, 10, 1, 5)
wood = Resource.Resource("Wood", 5, 10, 1, 5)
iron = Resource.Resource("Iron", 5, 10, 1, 5)

city1.add_resource(wheat, 100)
city1.add_resource(stone, 500)
city1.add_resource(wood, 70)
city1.add_resource(iron, 70)        # FIXED  Allows adding past maximum inventory size

city1.print_resources()

