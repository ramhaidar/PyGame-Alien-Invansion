import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class representing a single alien in the fleet."""

    def __init__(self, game):
        """Initialize alien and set starting position."""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        # Load alien image and set initial position
        self.image = pygame.image.load("images/alien1.png")
        self.rect = self.image.get_rect()

        # Start each alien near top-left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store exact horizontal position
        self.x = float(self.rect.x)

    def update(self):
        """Move alien right or left."""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """Return True if alien is at screen edge."""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right or 
                self.rect.left <= 0)
