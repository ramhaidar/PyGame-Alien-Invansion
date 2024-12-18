import pygame.font

class Button:
    """A class for game buttons."""

    def __init__(self, game, msg):
        """Initialize button attributes."""
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        # Configure button dimensions and properties
        self.width, self.height = 200, 50
        self.button_color = (70, 130, 180)  # Steel blue
        self.text_color = (255, 255, 255)   # White
        self.font = pygame.font.SysFont('arial', 48)

        # Build button rect and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # draw blank button and then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
