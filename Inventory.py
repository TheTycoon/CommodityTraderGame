import Resource


class Inventory:
    def __init__(self, size):
        self.inventory = []
        self.size = size
        self.empty = Resource.Resource("EMPTY", 0, 0, 0, 0)
        for x in range(size):
            self.inventory.append(self.empty)

    def print_inventory(self):
        for x in self.inventory:
            print(x.name)

    def check_empty_space(self):
        return self.inventory.count(self.empty)

    def add_item(self, item):
        if self.check_empty_space() > 0 and len(self.inventory) <= self.size:
            for x in range(self.size):
                if self.inventory[x] == self.empty:
                    self.inventory[x] = item
                    break
        else:
            print("DEBUG: INVENTORY FULL!")

    def remove_item(self, item):
        for x in range(self.size):
            if self.inventory[x] == item:
                self.inventory[x] = self.empty
                break

