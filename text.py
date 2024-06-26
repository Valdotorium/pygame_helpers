import pygame
import ui

def insertLineBreaks(text):
    cc = 0
    while cc < len(text):
        if cc % 12 == 0:
            text = text[:cc] + "\n" + text[cc:]
        cc += 1
class textbox():
    def __init__(self, x, y, color, bgcolor, text, font,fontsize, ticks, icon, animation):
        self.x = x
        self.y = y
        self.color = color
        self.bgcolor = bgcolor
        self.text = text
        self.font = pygame.font.SysFont(font, fontsize)
        self.textRect = self.font.render(text, True, color).get_rect()
        self.textRect.center = (self.x + self.textRect.width / 4, self.y)

        self.ticks = ticks
        self.icon = icon
        #for fade-in animation
        self.alpha = 0
        self.animation = animation
        if self.icon != None:
            #icon images must be square
            self.icon = pygame.transform.scale(self.icon,(self.textRect.height , self.textRect.height ))

    def draw(self, screen):
        surface = (self.font.render(self.text, True, self.color, self.bgcolor), self.textRect)
        #apply alpha
        if self.animation == "fade":
            surface[0].set_alpha(self.alpha)
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
        self.ticks -= 1
        screen.blit(surface[0], surface[1])
        if self.icon!= None:
            screen.blit(self.icon, (self.x - self.textRect.width / 2, self.y - self.textRect.height / 2))
class confirmMenu():
    def __init__(self, text ,font, fontsize,color, pos):
        self.text = text
        self.font = pygame.font.SysFont(font, fontsize)
        self.textbox = textbox(pos[0], pos[1], (255 - color[0], 255 - color[1], 255 - color[2]), color, text, font, 30, 1024, None, None)
        self.confirmButton = ui.staticButton(pos[0], pos[1] + self.textbox.textRect.height, self.textbox.textRect.width / 2, 50, color, "CONFIRM")
        self.cancelButton = ui.staticButton(pos[0] + self.textbox.textRect.width / 2, pos[1] + self.textbox.textRect.height, self.textbox.textRect.width / 2, 50, color, "CANCEL")
        self.status = None
    #check if the confirm or cancel button is being clicked
    def update(self, window):
        #if status is not none, delete self and button            self.textbox.draw(window)
        self.confirmButton.draw(window)
        self.cancelButton.draw(window)
        self.textbox.draw(window)
        if self.confirmButton.clicked:
            self.status = "confirm"
            del(self.cancelButton)
            del(self.confirmButton)
            del(self.textbox)
        elif self.cancelButton.clicked:
            self.status = "cancel"
            del(self.cancelButton)
            del(self.confirmButton)
            del(self.textbox)
        else:
            self.status = None

        return self.status
    

#function for text displaying
def DisplayText(text, font, fontsize, x, y):
    _textbox = textbox(x, y, (200,200,200),(95,85,80), text, font, fontsize, 180, None, None)
    return _textbox
    


#function for text warnings in the center of the screen
def warning(text, font,fontsize , icon):
    _textbox = textbox(400, 300, (200,200,200),(95,85,80), "    "+text, font,fontsize, 180, icon, "fade")
    return _textbox


#function for notification banners

