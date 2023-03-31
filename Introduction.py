import graphics
import settings


class Introduction:
    def __init__(self):
        # Create State Flags
        self.back_flag = False
        self.continue_flag = False
        # Create Buttons
        self.button_width = 100
        self.button_height = 50
        self.button_space = 75

        self.continue_button = graphics.Button((3 * settings.WIDTH / 4 - self.button_width / 2,
                                                settings.HEIGHT / 2 - self.button_height / 2,
                                                self.button_width, self.button_height),
                                                settings.BLUE, self.continue_function,
                                                text="Continue ->", hover_color=settings.RED)
        self.back_button = graphics.Button((settings.WIDTH / 4 - self.button_width / 2,
                                                settings.HEIGHT / 2 - self.button_height / 2,
                                                self.button_width, self.button_height),
                                               settings.BLUE, self.back_function,
                                               text="<- Back", hover_color=settings.RED)

    def continue_function(self):
        self.continue_flag = True

    def back_function(self):
        self.back_flag = True

    def introduction_events(self, event):
        # Send events to buttons to check if clicked
        self.continue_button.check_event(event)
        self.back_button.check_event(event)

    def introduction_draw(self, window):
        # Draw Text
        graphics.draw_text(window, "Introduction", 60, settings.BLACK, settings.WIDTH / 2,
                           settings.HEIGHT / 4, True)

        # Draw buttons
        self.continue_button.check_hover()
        self.continue_button.update(window)

        self.back_button.check_hover()
        self.back_button.update(window)





