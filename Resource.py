import random


class Resource:
    def __init__(self, name, sell_min, sell_max, buy_min, buy_max):
        self.name = name

        # This is the value the city will sell the resource for
        self.sell_price = int((sell_max + sell_min) / 2)
        self.sell_price_max = sell_max
        self.sell_price_min = sell_min

        # This is the value the city will buy the resource for
        self.buy_price = int((buy_max + buy_min) / 2)
        self.buy_price_max = buy_max
        self.buy_price_min = buy_min

    def new_day_sell(self):
        # Choose a random number to determine if the price goes up, down or stays the same
        sell_price_direction = random.randint(0, 10)

        # Change the price depending on the random number
        if sell_price_direction == 0:
            pass
        elif sell_price_direction % 2 == 0:
            self.sell_price += 1
        else:
            self.sell_price -= 1

        # Correct the price if it goes out of the range it belongs in
        if self.sell_price <= self.sell_price_min:
            self.sell_price = self.sell_price_min
        elif self.sell_price >= self.sell_price_max:
            self.sell_price = self.sell_price_max

    def new_day_buy(self):
        # Choose a random number to determine if the price goes up, down or stays the same
        buy_price_direction = random.randint(0, 10)

        # Change the price depending on the random number
        if buy_price_direction == 0:
            pass
        elif buy_price_direction % 2 == 0:
            self.buy_price += 1
        else:
            self.buy_price -= 1

        # Correct the price if it goes out of the range it belongs in
        if self.buy_price <= self.buy_price_min:
            self.buy_price = self.buy_price_min
        elif self.buy_price >= self.buy_price_max:
            self.buy_price = self.buy_price_max


# Think of a good way to initialize all resources at the start of running the program
# I am not using this code yet
def initialize_resources():
    wheat = Resource("Wheat", 5, 20, 1, 5)
    stone = Resource("Stone", 5, 20, 1, 5)
    wood = Resource("Wood", 5, 20, 1, 5)
    iron = Resource("Iron", 5, 20, 1, 5)
