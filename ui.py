import pygame

#basic animated text buttons
class Button():
    def __init__(self, x, y, width, height, color, text, animation):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.animation = animation
        self.font = pygame.font.SysFont("comicsans", 30)
        self.text_surface = self.font.render(self.text, True, (0, 0, 0))
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.center = (self.x + (self.width / 2), self.y + (self.height / 2))