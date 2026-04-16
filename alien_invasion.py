"""
Program: alien_invasion.py
Author: Kennett Aguilar-Zaldana
Purpose: Main module for the Alien Invasion game. Initializes the game, manages
the game loop, handles user input, and coordinates all game components.
Starter Code: Alien Invasion Starter - RedBeard41
https://github.com/RedBeard41/alien_Invasion_starter.git
Date: 04/08/26
"""

import sys
import pygame
from settings import Settings
from ship import Ship
from arsenal import Arsenal
# from alien import Alien
from alien_fleet import AlienFleet

class AlienInvasion:
    """Manges game resources, settings, and overall game behavior.
    """

    def __init__(self):
        """Initialize the game, display window, sounds, and core components.
        """
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_w,self.settings.screen_h)
            )
        pygame.display.set_caption("self.settings.name")

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg, 
            (self.settings.screen_w, self.settings.screen_h)
            )

        self.running = True
        self.clock = pygame.time.Clock()

        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)
        self.laser_sound.set_volume(0.7)

        
        self.ship = Ship(self, Arsenal(self))
        self.alien_fleet = AlienFleet(self)
        self.alien_fleet.create_fleet()

    def run_game(self):
        """Start and maintain the main game loop.
        """
        #Game Loop
        while self.running:
            self._check_events()
            self.ship.update()
            self.alien_fleet.update_fleet()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _update_screen(self):
        """Redraw the background, ship, and bullets on each frame.
        """
        self.screen.blit(self.bg, (0,0))
        self.ship.draw()
        self.alien_fleet.draw()
        pygame.display.flip()

    def _check_events(self):
        """Listen for and respond to keybond to keyboard and window events.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keyup_events(self, event):
        """Stop ship movement when a movement key is released.

        Args:
            event (pygame.event.Event): The keyboard event containing the 
            released key.
        """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


    def _check_keydown_events(self, event):
        """Handle ship movement, firing, and quitting on key press.

        Args:
            event (pygame.event.Event): The keyboard event containing the 
            pressed key.
        """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            if self.ship.fire():
                self.laser_sound.play()
                self.laser_sound.fadeout(250)

        elif event.key == pygame.K_q:
            self.running = False
            pygame.quit()
            sys.exit()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
