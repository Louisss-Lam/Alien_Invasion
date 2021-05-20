import pygame


class Pad:
    """A class to manage pad"""

    def __init__(self, ai_game):
        """Initalize the pad and set its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the pad image and get its rect.
        self.image = pygame.image.load("images/pad.bmp")
        self.rect = self.image.get_rect()

        # Start each new pad at the center of the screen.
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the pad at its current location."""
        self.screen.blit(self.image, self.rect)
