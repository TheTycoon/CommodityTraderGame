import Inventory
import Resource


class Player:
    def __init__(self):
        self.money = 1000
        self.inventory = Inventory.Inventory(5)

    def buy_item(self, item):
        if self.money >= item.sell_price and self.inventory.check_empty_space() > 0:
            self.money -= item.sell_price
            self.inventory.add_item(item)
        else:
            print("DEBUG: NOT ENOUGH MONEY or INVENTORY FULL!")

    def sell_item(self, item_index, city):
        for resource in city.inventory_buying.inventory:
            if self.inventory.inventory[item_index].name == resource.name:
                self.money += resource.buy_price
                self.inventory.inventory[item_index] = Resource.Resource("EMPTY", 0, 0, 0, 0)

    def print_inventory(self):
        count = 1
        for resource in self.inventory.inventory:
            print("{}. {}".format(count, resource.name))
            count += 1
