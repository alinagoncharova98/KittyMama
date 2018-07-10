import pygame, random

pygame.init()

display_width = 800
display_heigh = 1000

window = pygame.display.set_mode((display_width, display_heigh))

pygame.display.set_caption('KittyMama')

gameDisplay = pygame.Surface((display_width, display_heigh))

gameDisplay.fill((100, 100, 100))

surface = pygame.image.load("Луг.jpg")

done = True
while done:
    window.blit(surface, (0, 0))
    pygame.display.flip()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False








#class Player():
