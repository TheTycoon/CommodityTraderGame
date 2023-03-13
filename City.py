import Inventory


class City:
    def __init__(self, name, inventory_size):
        self.name = name
        self.inventory_size = inventory_size
        self.inventory = Inventory.Inventory(3)
        self.prices = dict()

    def add_resource(self, resource):
        self.inventory.inventory.append(resource)

    def set_prices(self):
        pass

        # self.cheapResourceName = cheap
        # self.expensiveResourceName = expensive
        # self.wildResourceName = wild

    # def print_resources(self):
    #     print("City: %s" % self.name)
    #     print("%s: " % self.cheapResourceName)
    #     print("%s: " % self.expensiveResourceName)
    #     print("%s: " % self.wildResourceName)


# city1 = City("New Startland", "Stone", "Wood", "Wheat")
# city1.print_resources()




