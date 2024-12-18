import pygame.font
from pygame.sprite import Group

from ship import Ship


class Scoreboard:
    """A class to manage scoring information."""

    def __init__(self, game):
        """Initialize scorekeeping attributes."""
        self.game = game
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.stats = game.stats

        # Font configuration
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.high_score_image = None
        self.high_score_rect = None
        self._initialize_score_images()

    def _initialize_score_images(self):
        """Initialize all score-related images."""
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Convert score into a rendered image."""
        rounded_score = round(self.stats.score, -1)
        score_str = "Score: " + f"{rounded_score:,}"
        self.score_image = self.font.render(score_str, True, 
                                          self.text_color, self.settings.bg_color)
        
        # Position the score
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "High Score: {:,}".format(high_score)
        
        # Create combined high score text and center it
        self.high_score_image = self.font.render(high_score_str, True, 
                                               self.text_color, self.settings.bg_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = 20

    def prep_level(self):
        """Turn the level into a rendered image."""
        level_str = "Level: " + str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

        # Position the level below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """Show how many ships are left."""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.game)
            ship.rect.x = 10 + ship_number * (ship.rect.width + 10)
            ship.rect.y = 20
            self.ships.add(ship)

    def check_high_score(self):
        """Check to see if there's a new high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def show_score(self):
        """Draw scores, level, and ships to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def show_high_score(self):
        """Draw the high score at the right of the screen."""
        high_score_str = "{:,}".format(self.stats.high_score)
        high_score_label = "High Score: " + high_score_str
        self.high_score_image = self.font.render(high_score_label, True,
                                               self.text_color, self.settings.bg_color)
        
        # Center high score at top of screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
