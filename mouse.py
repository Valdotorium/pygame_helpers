import pygame
class mouse():
    def __init__(self):
        self.pos = pygame.mouse.get_pos()
        self.state = pygame.mouse.get_pressed()
        self.click = False
        self.drag = False
        self.originOfTouch = self.pos
    #mouse function that returns the mouse position and state (False for no button clicked and True if a button is clicked)
    def update(self):
        self.pos = pygame.mouse.get_pos()
        self.state = pygame.mouse.get_pressed()[0]
        self.drag_detect()
        return self.pos, self.state
    
    #function that detects dragging and then outputs the mouse position when the drag ends.
    def drag_detect(self):
        if self.state == 1 and self.drag == False:
            self.originOfTouch = self.pos
            self.drag = True
        if self.state == 0 and self.drag == True:
            self.click = True
            self.drag = False
            return self.pos
        else:
            self.click = False
            return None

