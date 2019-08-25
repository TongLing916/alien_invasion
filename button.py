import pygame.font


class Button:

    def __init__(self, ai_settings, screen, msg):
        """initialize the attributes of a button"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # set the size of a button and others
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # set a rect for the button and put it in the center
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # only need to be created once
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """render msg as an image, and put it on the button"""
        self.msg_image = self.font.render(
            msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # draw a button filled with a color, and draw the text
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
