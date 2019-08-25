import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """a class to manage bullets from a space ship"""

    def __init__(self, ai_settings, screen, ship):
        """create an instance at the position of the ship"""
        super().__init__()
        self.screen = screen

        self.rect = pygame.Rect(
            0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """moving upwards"""
        # update bullet's position
        self.y -= self.speed_factor
        # update bullets's rect's position
        self.rect.y = self.y

    def draw_bullet(self):
        """draw bullet on a display"""
        pygame.draw.rect(self.screen, self.color, self.rect)
