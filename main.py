# Commodity Trader Game
# Buy/Sell Different Resources to Amass a Fortune
# Travel to Different Cities with Different Prices

import City
import Resource
import Player
import Engine
import pygame
import settings
import graphics

player = Player.Player()
city1 = City.City("New Startland", 3, 3)

# Think of a good way to initialize all resources at the start of running the program

# Adding test resources for the city to sell
wheat = Resource.Resource("Wheat", 5, 20, 0, 0)
stone = Resource.Resource("Stone", 5, 20, 0, 0)
wood = Resource.Resource("Wood", 5, 20, 0, 0)
city1.add_resource_sell(wheat)
city1.add_resource_sell(stone)
city1.add_resource_sell(wood)

# Adding test resources for the city to buy
rice = Resource.Resource("Wheat", 0, 0, 5, 20)          # Name is changed for testing purposes
iron = Resource.Resource("Iron", 0, 0, 5, 20)
cotton = Resource.Resource("Cotton", 0, 0, 5, 20)
city1.add_resource_buy(rice)
city1.add_resource_buy(iron)
city1.add_resource_buy(cotton)

# Testing buying items as player
player.buy_item(city1.inventory_selling.inventory[0])
player.buy_item(city1.inventory_selling.inventory[1])
player.buy_item(city1.inventory_selling.inventory[0])
player.buy_item(city1.inventory_selling.inventory[2])
player.buy_item(city1.inventory_selling.inventory[0])

# Simulate a number of days to change prices
city1.new_day()

# Testing selling items as player
player.sell_item(0, city1)

#   PYGAME STUFF BELOW
pygame.font.init()

# Set Up A Window
window = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
pygame.display.set_caption(settings.TITLE)

# Set Background Color
window.fill(settings.WHITE)

# MAIN LOOP
running = True
while running:

    # EVENT LOOP
    for event in pygame.event.get():

        # Close Program on Quit
        if event.type == pygame.QUIT:
            running = False

        # Check for Keys Pressed
        if event.type == pygame.KEYDOWN:

            # Press 1
            if event.key == pygame.K_1:
                pass

            # Press 2
            if event.key == pygame.K_2:
                pass

            # Press 3
            if event.key == pygame.K_3:
                pass

            # Press space
            if event.key == pygame.K_SPACE:
                pass

    # DRAW STUFF

    # Draw White Rectangle for Current City and Player Money
    pygame.draw.rect(window, settings.SILVER, pygame.Rect(0, 0, settings.WIDTH, 100))

    # Draw Current City and Player Money
    graphics.draw_text(window, "Current City: " + city1.name, 26, settings.BLACK, 0, 0, False)
    graphics.draw_text(window, "Player Money: " + str(player.money), 26, settings.BLACK, 0, 30, False)

    # Print Player Inventory
    pygame.draw.rect(window, settings.BLACK, pygame.Rect(0, 100, settings.WIDTH / 2, 200))
    graphics.draw_text(window, "Player Inventory", 26, settings.WHITE, 0, 100, False)
    player.draw_inventory(window)

    # Draw Rectangle Example
    # pygame.draw.rect(window, color, pygame.Rect(x pos, y pos, width, height)
    # pygame.draw.rect(window, settings.BLUE, pygame.Rect(0, 0, 100, 100))

    # DISPLAY FRAME
    pygame.display.update()



#Engine.main_menu(city1)




#
#
# player.print_inventory()
# print(player.money)

