import pygame

#basic animated text buttons
class Button():
    def __init__(self, x, y, width, height, color, text, animation):
        #the center coordinates
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        #when the button gets hovered, it gets brighter
        self.bright = (self.color[0] + (255 - self.color[0]) / 8,self.color[1] + (255 - self.color[1]) / 8,self.color[2] + (255 - self.color[2]) / 8 )
        #original color value backup
        self.dark = self.color
        self.text = text
        self.animation = animation
        self.font = pygame.font.SysFont("arial", 30)
        self.text_surface = self.font.render(self.text, True, (0, 0, 0))
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.center = (self.x + (self.width / 2), self.y + (self.height / 2))
        self.clicked = False
        self.ticksInAnimation = 0
        self.hovered = False
        self.originalWidth = self.width
        self.originalHeight = self.height
    #now create a function that makes a button that detects when it its clicked and/or hovered
    def animate(self):
        if self.animation == "plop":
            print(self.color)
            #for 10 frames, the button gets bigger
            if 0 < self.ticksInAnimation < 10:
                self.width = self.originalWidth + self.originalWidth * self.ticksInAnimation /50
                self.height = self.originalHeight + self.originalHeight * self.ticksInAnimation / 50
            elif 9 < self.ticksInAnimation:
                # after that, it stays 20% bigger than normal until
                self.width = self.originalWidth * 1.2
                self.height = self.originalHeight * 1.2
            else:
                #it is not hovered anymore
                self.width = self.originalWidth
                self.height = self.originalHeight
        if self.animation == "expand":
            
            if 1 < self.ticksInAnimation:
                # The button stays 20% bigger than normal until
                self.width = self.originalWidth * 1.2
                self.height = self.originalHeight * 1.2
            else:
                #it is not hovered anymore
                self.width = self.originalWidth
                self.height = self.originalHeight
        if self.animation == "none":
            pass
    
    def draw(self, window):
        self.text_rect.center = (self.x, self.y)
        self.animate()
        pygame.draw.rect(window, self.color, (int(self.x - self.width/2), self.y -int(self.height/2), int(self.width), int(self.height)))
        window.blit(self.text_surface, self.text_rect)
        #now it should detect if it is hovered
        if pygame.mouse.get_pos()[0] > self.x - self.width/2 and pygame.mouse.get_pos()[0] < self.x + self.width/2 and pygame.mouse.get_pos()[1] > self.y-self.height/2 and pygame.mouse.get_pos()[1] < self.y + self.height/2:
            self.color = self.bright
            self.hovered = True
            self.ticksInAnimation +=1
            #now detect clicks
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.color = self.bright
            else:
                self.clicked = False
        else:
            self.color = self.dark
            self.hovered = False
            self.ticksInAnimation = 0
        
            

