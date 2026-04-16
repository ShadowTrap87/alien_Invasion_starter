"""
Program: game_stats.py
Author: Kennett Aguilar-Zaldana
Purpose: Tracks game stats such as remaining ships (lives) for the Alien Invasion game.
Starter Code: None
Date: 04/16/26
"""
class GameStats():
    """Tracks stats for the game, such as remaining ships/lives.
    """

    def __init__(self, ship_limit):
        """Initialize game stats.

        Args:
            ship_limit (int): The number of ships (lives) the player starts with.
        """
        self.ship_left = ship_limit
        
