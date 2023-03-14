import random


class Resource:
    def __init__(self, name, sell_min, sell_max, buy_min, buy_max):
        self.name = name

        # This is the value the city will sell the resource for
        self.sell_price = (sell_max + sell_min) / 2
        self.sell_price_max = sell_max
        self.sell_price_min = sell_min

        # This is the value the city will buy the resource for
        self.buy_price = (buy_max + buy_min) / 2
        self.buy_price_max = buy_max
        self.buy_price_min = buy_min

    def new_day(self):
        # Choose a random number to determine if the price goes up, down or stays the same
        sell_price_direction = random.randint(0, 10)
        print("Sell Direction: %s" % sell_price_direction)

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
