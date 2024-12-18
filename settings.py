import pygame


class Settings:
    """Class to store all settings for Alien Invasion game."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Display settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)  # Light blue background

        # Ship settings 
        self.ship_limit = 3
        
        # Bullet configurations
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 10

        # Game scaling settings
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.alien_points = 50

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change during gameplay."""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        self.fleet_direction = 1  # 1 represents right, -1 represents left
        self.alien_points = 25

    def increase_speed(self):
        """Increase game speed and point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
