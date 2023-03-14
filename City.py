import Inventory


class City:
    def __init__(self, name, inventory_size):
        self.name = name
        self.inventory_size = inventory_size
        self.inventory = Inventory.Inventory(inventory_size)
        self.amounts = dict()

    def add_resource(self, resource, amount):
        self.inventory.add_item(resource)
        if len(self.amounts) < self.inventory_size:
            self.amounts.update({resource.name: amount})

    def set_prices(self):
        pass

    def print_resources(self):
        print("===========================")
        print("City: {}".format(self.name))
        print("===========================")
        print()
        # self.inventory.print_inventory()      Not needed if printing dictionary
        print(self.amounts)

    def print_inventory_sell(self):
        pass

    def print_inventory_buy(self):
        pass







