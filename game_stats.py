class GameStats:
    """Track statistics and scoring for Alien Invasion."""

    def __init__(self, game):
        """Initialize game statistics."""
        self.settings = game.settings
        self.reset_stats()
        
        # Start game in inactive state
        self.game_active = False
        
        # High score should persist between sessions
        self.high_score = 0

    def reset_stats(self):
        """Initialize dynamic statistics."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
        
    def _load_high_score(self):
        """Load high score from storage if available."""
        try:
            with open('highscore.txt', 'r') as f:
                return int(f.read())
        except:
            return 0
