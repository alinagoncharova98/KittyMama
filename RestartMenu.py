import pygame

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

myfont = pygame.font.SysFont("comicsansms", 16)
score = 0

def text_objects(text, font):
    textSurface = font.render(text, True, [255, 255, 255])
    return textSurface, textSurface.get_rect()


def button (msg, x, y, w, h, ic, ac, action=None ):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if (x+w > mouse[0] > x) and (y+h > mouse[1] > y):
        pygame.draw.rect(window, (0,0,0), (x, y, w, h))
        if (click[0] == 1 and action != None):
            if  (action == "Start"):
                import Game
                Game.game_loop()
            elif (action == "Exit"):
                pygame.quit()
    else:
        pygame.draw.rect(window, (0,0,0), (x, y, w, h))
        smallText = pygame.font.SysFont("comicsansms", 50)
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = ( (x+(w/2)), (y+(h/2)) )
        window.blit(textSurf, textRect)

done = True
while done:
    window.blit(surface, (0, 0))

    scoretext = myfont.render("Your score {0}".format(score), 1, (0, 0, 0))
    window.blit(scoretext, (5, 10))
    score += 1

    button("Restart", 600, 120, 120, 25, (255, 255, 255),(0, 0, 0),  "Start")
    button("Exit", 600, 620, 120, 25, (0, 0, 0), (255, 255, 255), "Exit")
    pygame.display.update()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False


    clock.tick(40)
pygame.quit()
quit()

