# Functions to help drive the game
import settings
import graphics
import pygame
import Introduction


pygame.font.init()

# Set Up A Window

pygame.display.set_caption(settings.TITLE)


class Engine:
    def __init__(self):
        self.window = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
        self.window.fill(settings.WHITE)
        self.running = True
        self.current_state = "Main Menu"

        self.introduction = Introduction.Introduction()

        # Create Buttons For Menu
        self.button_width = 100
        self.button_height = 50
        self.button_space = 75

        self.start_button = graphics.Button((settings.WIDTH / 2 - self.button_width / 2,
                                             settings.HEIGHT / 2 - self.button_height / 2,
                                             self.button_width, self.button_height), settings.BLUE, self.test_function,
                                             text="Start New Game", hover_color=settings.RED)

        self.quit_button = graphics.Button((settings.WIDTH / 2 - self.button_width / 2,
                                            settings.HEIGHT / 2 - self.button_height / 2 + self.button_space,
                                            self.button_width, self.button_height),
                                            settings.BLUE, self.stop_running,
                                            text="Quit", hover_color=settings.RED)

    def test_function(self):
        print("Testing")

    def stop_running(self):
        self.running = False

    def main_loop(self):
        while self.running:

            # EVENT LOOP
            for event in pygame.event.get():

                # self.main_menu_events(event)
                self.introduction.introduction_events(event)

                # Close Program on Quit
                if event.type == pygame.QUIT:
                    self.stop_running()

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
                        # Simulate a day to change prices
                        # city1.new_day()

            # DRAW EVERYTHING TO THE SCREEN FOR 1 FRAME

            # Check The State Before Drawing

            # Draw main menu
            # self.main_menu_draw(self.window)
            self.introduction.introduction_draw(self.window)

            # # Draw White Rectangle for Current City and Player Money
            # pygame.draw.rect(window, settings.SILVER, pygame.Rect(0, 0, settings.WIDTH, 100))
            #
            # # Draw Current City and Player Money
            # graphics.draw_text(window, "Current City: " + city1.name, 26, settings.BLACK, 0, 0, False)
            # graphics.draw_text(window, "Player Money: " + str(player.money), 26, settings.BLACK, 0, 30, False)
            #
            # # Print Player Inventory
            # pygame.draw.rect(window, settings.BLACK, pygame.Rect(0, 100, settings.WIDTH / 2, 200))
            # graphics.draw_text(window, "Player Inventory", 26, settings.WHITE, 0, 100, False)
            # player.draw_inventory(window)
            #
            # # Draw Test Button
            # test_button.check_hover()
            # test_button.update(window)
            #
            # # Draw Rectangle Example
            # # pygame.draw.rect(window, color, pygame.Rect(x pos, y pos, width, height)
            # # pygame.draw.rect(window, settings.BLUE, pygame.Rect(0, 0, 100, 100))

            # DISPLAY FRAME
            pygame.display.update()

    def main_menu_events(self, event):
        # Send events to buttons to check if clicked
        self.quit_button.check_event(event)
        self.start_button.check_event(event)

    def main_menu_draw(self, window):
        # Draw Title
        graphics.draw_text(window, "Commodity Trader Game", 60, settings.BLACK, settings.WIDTH / 2,
                           settings.HEIGHT / 4, True)

        # Draw main menu buttons
        self.start_button.check_hover()
        self.start_button.update(window)

        self.quit_button.check_hover()
        self.quit_button.update(window)
