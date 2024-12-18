import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage projectiles fired from the ship."""

    def __init__(self, game):
        """Create bullet object at ship's position."""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        # Create bullet and set position
        self.rect = pygame.Rect(0, 0, 
            self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midtop = game.ship.rect.midtop

        # Store precise position
        self.y = float(self.rect.y)
        self.color = self.settings.bullet_color

    def update(self):
        """Move the bullet up the screen."""
        # update the decimal position of the bullet.
        self.y -= self.settings.bullet_speed
        # update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
