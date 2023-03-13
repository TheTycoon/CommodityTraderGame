class Inventory:
    def __init__(self, size):
        self.inventory = []
        self.size = size
        for x in range(size):
            self.inventory.append("EMPTY")

    def print_inventory(self):
        for x in self.inventory:
            print(x)

    def check_empty_space(self):
        return self.inventory.count("EMPTY")

    def add_item(self, item):
        if self.check_empty_space() > 0:
            for x in range(self.size):
                if self.inventory[x] == "EMPTY":
                    self.inventory[x] = item
                    break
        else:
            print("Inventory Full!")

    def remove_item(self, item):
        for x in range(self.size):
            if self.inventory[x] == item:
                self.inventory[x] = "EMPTY"
                break




# PLANNING


#print(inventory.count("EMPTY"))

# Restrict Inventory Size
#while len(inventory) > maxInventory:
    #inventory.pop()

