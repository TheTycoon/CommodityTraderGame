import Inventory


class Player:
    def __init__(self):
        self.money = 1000
        self.inventory = Inventory.Inventory(5)

    def buy_item(self, item):
        pass

