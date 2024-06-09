import mouse
import text
import ui
import pygame


#function that initializes pygame and prints the state of the mouse
def init():
    pygame.init()
    #make a window
    window = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("test")
    #make a clock
    clock = pygame.time.Clock()
    return window, clock



window, clock = init()
mouse = mouse.mouse()
while True:
    window.fill((255, 255, 255))
    pygame.display.update()
    clock.tick(60)
    mouse.update()
    print("state:", mouse.state, "click:",mouse.click, "pos:",mouse.pos, "origin:", mouse.originOfTouch)
    #quitting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
