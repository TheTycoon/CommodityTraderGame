import random


class Resource:
    def __init__(self, name):
        self.Name = "Stone"

        # This is the value the city will sell the resource for
        self.sell_price = 5
        self.sell_price_max = 10
        self.sell_price_min = 5

        # This is the value the city will buy the resource for
        self.buy_price = 1
        self.buy_price_max = 5
        self.buy_price_min = 1

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
