import graphics
import settings


class Introduction:
    def __init__(self):
        # Create Buttons
        self.button_width = 100
        self.button_height = 50
        self.button_space = 75

        self.continue_button = graphics.Button((settings.WIDTH / 2 - self.button_width / 2,
                                                settings.HEIGHT / 2 - self.button_height / 2,
                                                self.button_width, self.button_height),
                                                settings.BLUE, self.test_function,
                                                text="Continue ->", hover_color=settings.RED)

    def test_function(self):
        pass

    def introduction_events(self, event):
        # Send events to buttons to check if clicked
        self.continue_button.check_event(event)

    def introduction_draw(self, window):
        # Draw Text
        graphics.draw_text(window, "Introduction", 60, settings.BLACK, settings.WIDTH / 2,
                           settings.HEIGHT / 4, True)

        # Draw buttons
        self.continue_button.check_hover()
        self.continue_button.update(window)





