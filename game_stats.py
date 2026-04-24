"""
Program: game_stats.py
Author: Kennett Aguilar-Zaldana
Purpose: Tracks game stats such as remaining ships (lives) for the Alien Invasion game.
Starter Code: None
Date: 04/16/26
"""

# from pathlib import Path
import json

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class GameStats():
    """Tracks stats for the game, such as remaining ships/lives.
    """

    def __init__(self, game: 'AlienInvasion'):
        """Initialize game stats and load saved scores.

        Args:
            game (AlienInvasion): The main game instance.
        """
        self.game = game
        self.settings = game.settings
        self.max_score = 0
        self.init_saved_scores()
        self.reset_stats()

    def init_saved_scores(self):
        """Load the high score from file, or initialize it to zero if not found.
        """
        self.path = self.settings.scores_file
        if self.path.exists() and self.path.stat.__sizeof__() > 20:
            contents = self.path.read_text()
            scores = json.loads(contents)
            self.hi_score = scores.get('hi_score', 0)
        else:
            self.hi_score = 0
            self.save_scores()
            # save the file

    def save_scores(self):
        """Save the current high score to the scores file.
        """
        scores = {
            'hi_score': self.hi_score
        }
        contents = json.dumps(scores, indent=4)
        try:
            self.path.write_text(contents)
        except FileNotFoundError as e:
            print(f'File Not Found: {e}')

    def reset_stats(self):
        """Reset all game stats to their starting values.
        """
        self.ship_left = self.settings.starting_ship_count
        self.score = 0
        self.level = 1

    def update(self, collisions):
        """Update score, max score, and high score based on collisions.

        Args:
            collisions (dict): Dictionary of collision results from pygame.
        """
        # update self
        self._update_score(collisions)
        # update max_score
        self._update_max_score()
        
        # update hi_score
        self._update_hi_score()

    def _update_max_score(self):
        """Update the max score if the current score exceeds it.
        """
        if self.score > self.max_score:
            self.max_score = self.score
        # print(f'Max: {self.max_score}')

    def _update_hi_score(self):
        """Update the high score if the current score exceeds it.
        """
        if self.score > self.hi_score:
            self.hi_score = self.score
        # print(f'Hi: {self.hi_score}')



    def _update_score(self, collisions):
        """Add points for each alien destroyed.

        Args:
            collisions (dict): Dictionary of collision results from pygame.
        """
        for alien in collisions.values():
            self.score += self.settings.alien_points
        # print(f'Basic: {self.score}')

    def update_level(self):
        """Increment the current level by one.
        """
        self.level += 1
        print(self.level)
    
        
