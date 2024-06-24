import pygame


class textbox():
    def __init__(self, x, y, color, bgcolor, text, font,fontsize, ticks, icon):
        self.x = x
        self.y = y
        self.color = color
        self.bgcolor = bgcolor
        self.text = text
        self.font = pygame.font.SysFont(font, fontsize)
        self.textRect = self.font.render(text, True, color).get_rect()
        self.textRect.center = (self.x, self.y)
        self.ticks = ticks
        self.icon = icon
        #for fade-in animation
        self.alpha = 0
        if self.icon != None:
            #icon images must be square
            self.icon = pygame.transform.scale(self.icon,(self.textRect.height , self.textRect.height ))

    def draw(self, screen):
        surface = (self.font.render(self.text, True, self.color, self.bgcolor), self.textRect)
        #apply alpha
        surface[0].set_alpha(self.alpha)
        screen.blit(surface[0], surface[1])
        if self.ticks > 13:
            self.alpha += 15
            if self.alpha > 255:
                self.alpha = 255
        else:
            self.alpha -= 20
            if self.alpha < 0:
                self.alpha = 0

        if self.icon!= None:
            # apply alpha to icon
            self.icon.set_alpha(self.alpha)
            #blit icon to the screen
            screen.blit(self.icon, (self.x - self.textRect.width / 2, self.y - self.textRect.height / 2))
        self.ticks -= 1
        
#function for text displaying
def DisplayText(text, font, fontsize, x, y):
    _textbox = textbox(x, y, (200,200,200),(95,85,80), text, font, fontsize, 180, None)
    return _textbox

    


#function for text warnings in the center of the screen
def warning(text, font,fontsize , icon):
    _textbox = textbox(400, 300, (200,200,200),(95,85,80), "    "+text, font,fontsize, 180, icon)
    return _textbox


#function for notification banners

