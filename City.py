import Inventory


# Cities currently have an unlimited amount of goods they will buy and sell
class City:
    def __init__(self, name, inventory_size_sell, inventory_size_buy):
        self.name = name
        self.inventory_size_sell = inventory_size_sell
        self.inventory_size_buy = inventory_size_buy
        self.inventory_selling = Inventory.Inventory(inventory_size_sell)
        self.inventory_buying = Inventory.Inventory(inventory_size_buy)

    def add_resource(self, resource):
        self.inventory_selling.add_item(resource)

    def set_prices(self):
        pass

    # will this even be necessary? just do the sell and buy functions instead
    def print_resources(self):
        print("===========================")
        print("City: {}".format(self.name))
        print("===========================")
        print()

    def print_inventory_sell(self):
        for resource in self.inventory_selling.inventory:
            print("{}: {} Gold".format(resource.name, resource.sell_price))

    def print_inventory_buy(self):
        pass

    def new_day(self):
        for resource in self.inventory_selling.inventory:
            resource.new_day()







