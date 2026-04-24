"""
Program: alien.py
Author: Kennett Aguilar-Zaldana
Purpose: Defines the Alien class which represents a single alien enemy 
in the Alien Invasion game. Handles movement, edge detection, and drawing.
Starter Code: None
Date: 04/08/26
"""

import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_fleet import AlienFleet

class Alien(Sprite):
    """Represents a single alien in the Alien Invasion game.

    Args:
        Sprite (pygame.sprite.Sprite): Base sprite class.
    """
    def __init__(self, fleet: 'AlienFleet', x: float, y: float):
        """Initialize an alien at the given position within the fleet

        Args:
            fleet (AlienFleet): The alien fleet this alien belongs to.
            x (float): Initial x-coordinate.
            y (float): Initial y-coordinate.
        """
        super().__init__()
        self.fleet = fleet
        self.screen = fleet.game.screen
        self.boundaries = fleet.game.screen.get_rect()
        self.settings = fleet.game.settings

        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(self.image, 
            (self.settings.alien_w, self.settings.alien_h)
            )
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self):
        """Update the alien's horizontal position based on fleet direction.
        """
        temp_speed = self.settings.fleet_speed

        self.x += temp_speed * self.fleet.fleet_direction
        self.rect.x = self.x
        self.rect.y = self.y

    def check_edges(self):
        """Check if the alien has reached the screen edge.

        Returns:
            bool: True if the alien hits the left or right boundary.
        """
        return (self.rect.right >= self.boundaries.right or self.rect.left <= self.boundaries.left)

    def draw_alien(self):
        """Draw the alien onto the screen.
        """
        self.screen.blit(self.image, self.rect)
