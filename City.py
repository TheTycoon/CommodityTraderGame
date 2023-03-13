import Inventory


class City:
    def __init__(self, name, inventory_size):
        self.name = name
        self.inventory_size = inventory_size
        self.inventory = Inventory.Inventory(inventory_size)
        self.prices = dict()

    def add_resource(self, resource):
        self.inventory.inventory.append(resource)

    def set_prices(self):
        pass

    def print_resources(self):
        pass







