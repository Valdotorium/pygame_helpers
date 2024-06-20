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
button = ui.Button(200,200,100,50,(100,70,70), "Hi", "expand")
textbox = text.warning("Hio", "Arial",32, pygame.image.load("icons/wheelNew.png"))
while True:
    window.fill((255, 255, 255))
    clock.tick(60)
    mouse.update()
    button.draw(window)


    if textbox.ticks <= 0:
       pass
    else:
        textbox.draw(window)

    pygame.display.update()
    print("state:", mouse.state, "click:",mouse.click, "pos:",mouse.pos, "origin:", mouse.originOfTouch)
    #quitting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
