import pygame, random, os


class GameObject:
    def __init__(self, image, height, speed):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect().move(0, height)

    def move(self):
        self.pos = self.pos.move(self.speed, 0)
        if self.pos.right > 600:
            self.pos.left = 0


def load_image(name):
    image = pygame.image.load(name).convert_alpha()
    image = pygame.transform.scale(image,(int(image.get_rect().size[0]/2),int(image.get_rect().size[1]/2)))
    return image


pygame.init()
display_width = 500
display_heigh = 680
window = pygame.display.set_mode((display_width, display_heigh))
pygame.display.set_caption('KittyMama')
gameDisplay = pygame.Surface((display_width, display_heigh))
surface = load_image('back.jpg')
surface = pygame.transform.scale(surface, (display_width, display_heigh))
window.blit(surface, (0,0))
pygame.display.flip()

cat1 = load_image('cat1.png')
cat2 = load_image('cat2.png')
cat3 = load_image('cat3.png')
cat4 = load_image('cat4.png')
basket_img = load_image('basket.png')
cats = [cat1, cat2, cat3, cat4]

x_cat = random.randint(int(97/2), int(display_width - 97/2))
y_cat = -160
y_change = 0

def basket(x, y):
    window.blit(basket_img, (x, y))

def cat(x, y):
    #c = random.randint(0, 3)
    window.blit(cat1, (x,y))



x = display_width / 2 - 50
y = display_heigh - 259/2
x_change = 0

clock = pygame.time.Clock()
end = False

while not end:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if x > 3:
                    x_change = -4
                else:
                    x_change = 0
            elif event.key == pygame.K_RIGHT:
                if x < display_width - 213/2 - 3:
                    x_change = 4
                else:
                    x_change = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0

    if x >= 0 and x <= display_width - 213 / 2:
        x += x_change

    window.blit(surface, (0, 0))
    if y_cat < display_heigh:
        y_change = 5
    else:
        y_cat = -160
        x_cat = random.randrange(50, 550)
    y_cat += y_change
    cat(x_cat, y_cat)
    basket(x, y)
    if x < 0:
        x += 4
    elif x > display_width - 213/2:
        x -= 3

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
