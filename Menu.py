import pygame, random, time

pygame.init()

display_width = 900
display_heigh = 1200

window = pygame.display.set_mode((display_width, display_heigh))

pygame.display.set_caption('KittyMama')

clock = pygame.time.Clock()

gameDisplay = pygame.Surface((display_width, display_heigh))
surface = pygame.image.load("1.jpg")
window.blit(surface, (0, 0))
pygame.display.flip()



def text_objects(text, font):
    textSurface = font.render(text, True, [255, 255, 255])
    return textSurface, textSurface.get_rect()


def button (disp, msg, x, y, w, h, ic, ac, action=None ):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if (x+w > mouse[0] > x) and (y+h > mouse[1] > y):
        pygame.draw.rect(disp, (0,0,0), (x, y, w, h))
        if (click[0] == 1 and action != None):
            if  (action == "Start"):
                game_loop()
            #elif  (action == "Load"):
                 ##Function that makes the loading of the saved file##

            elif (action == "Exit"):
                pygame.quit()

    else:
        pygame.draw.rect(disp, (0,0,0), (x, y, w, h))
        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = ( (x+(w/2)), (y+(h/2)) )
        disp.blit(textSurf, textRect)

def game_loop():
    print('hfdh')

done = True
while done:
    #button(gameDisplay,"Start", 600, 120, 120, 25, (255, 255, 255),(0, 0, 0),  "Start")
    #button(gameDisplay,"Exit", 600, 620, 120, 25, (0, 0, 0), (255, 255, 255), "Exit")

    pygame.draw.rect(gameDisplay, (0, 255, 0), (500, 500, 600, 25))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False


    #clock.tick(40)
pygame.quit()
quit()

