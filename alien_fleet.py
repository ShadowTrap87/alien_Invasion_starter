"""
Program: alien_fleet.py
Author: Kennett Aguilar-Zaldana
Purpose: Manages the creation, movement, rendering, and collision behavior 
of the alien fleet in the Alien Invasion game.
Starter Code: None
Date: 04/16/26
"""

import pygame
from alien import Alien
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class AlienFleet:
    """Manages the alien fleet, including creation, movement, drawing,
    and collision behavior in the Alien Invasion game.
    """
    
    def __init__(self, game: 'AlienInvasion'):
        """Initialize the alien fleet and set up game references.

        Args:
            game (AlienInvasion): The main game instance.
        """
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = self.settings.fleet_direction
        self.fleet_drop_speed = self.settings.fleet_drop_speed


        self.create_fleet()

    def create_fleet(self):
        """Create a full fleet of aliens based on screen size and settings.
        """
        alien_w = self.settings.alien_w
        alien_h = self.settings.alien_h
        screen_w = self.settings.screen_w
        screen_h = self.settings.screen_h

        fleet_w, fleet_h = self.calculate_fleet_size(alien_w, screen_w, alien_h, screen_h)
        x_offset, y_offset = self.calculate_offsets(alien_w, alien_h, screen_w, fleet_w, fleet_h)
        
        self._create_rectangle_fleet(alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset)

    def _create_rectangle_fleet(self, alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset):
        """Create aliens in a grid formation.

        Args:
            alien_w (int): Width of aliens.
            alien_h (int): Height of aliens.
            fleet_w (int): Number of aliens per row.
            fleet_h (int): Number of rows.
            x_offset (int): Horizontal starting position.
            y_offset (int): Vertical starting position.
        """
        for row in range(fleet_h):
            for col in range(fleet_w):
                current_x = alien_w * col + x_offset
                currnet_y = alien_h * row + y_offset
                if col % 2 == 0 or row % 2 == 0:
                    continue
                self._create_alien(current_x, currnet_y)

    def calculate_offsets(self, alien_w, alien_h, screen_w, fleet_w, fleet_h):
        """Calculate starting position offsets for centering the fleet.

        Returns:
            tuple[int, int]: (x_offset, y_offset)
        """
        half_screen = self.settings.screen_h//2
        fleet_horizontal_space = fleet_w * alien_w
        fleet_vertical_space = fleet_h * alien_h
        x_offset = int((screen_w-fleet_horizontal_space)//2)
        y_offset = int((half_screen-fleet_vertical_space)//2)
        return x_offset,y_offset

    
    def calculate_fleet_size(self, alien_w, screen_w, alien_h, screen_h):
        """Calculate how many aliens fit horizontally and vertically.

        Returns:
            tuple[int, int]: (fleet_width, fleet_height)
        """
        fleet_w = (screen_w//alien_w)
        fleet_h = ((screen_h /2)//alien_h)

        if fleet_w % 2 == 0:
            fleet_w -= 1
        else:
            fleet_w -= 2

        if fleet_h % 2 == 0:
            fleet_h -= 1
        else:
            fleet_h -= 2


        return int(fleet_w), int(fleet_h)
    

    def _create_alien(self, current_x: int, currnet_y:int):
        """Create a single alien and add it to the fleet.

        Args:
            current_x (int): X position.
            currnet_y (int): Y position.
        """
        new_alien = Alien(self, current_x, currnet_y)
                          
        self.fleet.add(new_alien)

    def _check_fleet_edges(self):
        """Check if any alien has reached an edge and update direction.
        """
        alien: Alien
        for alien in self.fleet:
            if alien.check_edges():
                self._drop_alien_fleet()
                self.fleet_direction *= -1
                break


    def _drop_alien_fleet(self):
        """Move the entire fleet down.
        """
        for alien in self.fleet:
            alien.y += self.fleet_drop_speed


    def update_fleet(self):
        """Update fleet position and handle edge collisions.
        """
        self._check_fleet_edges()
        self.fleet.update()


    def draw(self):
        """Draw all aliens on the screen.
        """
        alien: 'Alien'
        for alien in self.fleet:
            alien.draw_alien()

    def check_collisions(self, other_group):
        """Check for collisions between aliens and another sprite group.

        Args:
            other_group (pygame.sprite.Group): Group to check collisions with.

        Returns:
            dict: Collision results from pygame.sprite.groupcollide.
        """
        return pygame.sprite.groupcollide(self.fleet, other_group, True, True)
    
    def check_fleet_bottom(self):
        """Check if any alien has reached the bottom of the screen.

        Returns:
            bool: True if an alien hits the bottom, otherwise False.
        """
        alien: Alien
        for alien in self.fleet:
            if alien.rect.bottom >= self.settings.screen_h:
                return True
        return False
    
    def check_destroyed_status(self):
        """Check if the fleet has been completely destroyed.

        Returns:
            bool: True if no aliens remain.
        """
        return not self.fleet