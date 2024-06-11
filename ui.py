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
        self.clicked = False
        self.ticksInAnimation = 0
        self.hovered = False
    #now create a function that makes a button that detects when it its clicked and/or hovered
    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))
        window.blit(self.text_surface, self.text_rect)
        #now it should detect if it is hovered
        if pygame.mouse.get_pos()[0] > self.x and pygame.mouse.get_pos()[0] < self.x + self.width and pygame.mouse.get_pos()[1] > self.y and pygame.mouse.get_pos()[1] < self.y + self.height:
            self.color = (100, 100, 100)
            self.hovered = True
            #now detect clicks
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.color = (100, 70, 70)
            else:
                self.clicked = False
        else:
            self.color = (100, 70, 70)
            self.hovered = False
            

