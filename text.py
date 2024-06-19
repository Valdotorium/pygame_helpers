import pygame


class textbox():
    def __init__(self, x, y, color, text, font, ticks, icon):
        self.x = x
        self.y = y
        self.color = color
        self.text = text
        self.font = pygame.font.SysFont(font, 20)
        self.textRect = self.font.render(text, True, color).get_rect()
        self.textRect.center = (self.x, self.y)
        self.ticks = ticks
        self.icon = icon
        if self.icon != None:
            #icon images must be square
            self.icon = pygame.transform.scale(self.icon(self.textRect.get_height / 2, self.textRect.get_height / 2))


    def draw(self, screen):
        screen.blit(self.font.render(self.text, True, self.color, (110, 105, 90)), self.textRect)
        self.ticks -= 1
        if self.ticks == 0:
            del(self)
#function for text displaying
def DisplayText(screen, text, font, color, x, y):
    _textbox = textbox(x, y, color, text, font, 180, None)
    return _textbox
    


#function for text warnings in the center of the screen



#function for notification banners

