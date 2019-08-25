import pygame


class Ship():

    def __init__(self, ai_settings, screen):
        """initialize spaceship and its orignal position"""
        self.screen = screen
        self.ai_settings = ai_settings

        # load spaceship image and get its rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # put every new spaceship in the center bottom
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # store small value in "center"
        self.center = float(self.rect.centerx)

        # moving flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """adjust ship's position according to the moving_flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # udpate rect according to self.center
        self.rect.centerx = self.center

    def blitme(self):
        """draw spaceshil at a given position"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """center the ship"""
        self.center = self.screen_rect.centerx
