"""
Program: button.py
Author: Kennett Aguilar-Zaldana
Purpose: Defines the Button class which renders a clickable play button
on the game screen.
Starter Code: None
Date: 04/23/26

"""

import pygame.font

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    
class Button:
    """Represents a clickable button displayed on the game screen.
    """

    def __init__(self, game: 'AlienInvasion', msg):
        """Initialize the button with text and position it at screen center.

        Args:
            game (AlienInvasion): The main game instance.
            msg (str): The text to display on the button.
        """
        self.game = game
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.settings = game.settings
        self.font = pygame.font.Font(self.settings.font_file, 
            self.settings.button_font_size)
        self.rect = pygame.Rect(0,0,self.settings.button_w, self.settings.button_h)
        self.rect.center = self.boundaries.center
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Render the button message as an image centered on the button.

        Args:
            msg (str): The text to render on the button.
        """
        self.msg_image = self.font.render(msg, True, self.settings.text_color, None)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        """Draw the button and its text to the screen.
        """
        self.screen.fill(self.settings.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def check_clicked(self, mouse_pos):
        """Check if the button was clicked.

        Args:
            mouse_pos (tuple): The current mouse position.

        Returns:
            bool: True if the button was clicked, otherwise False.
        """
        return self.rect.collidepoint(mouse_pos)