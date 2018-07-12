import pygame, random, os


class Gameobject:
    def __init__(self, b_image, speed, coord_x, coord_y):
        self.b_image = b_image
        self.speed = speed
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.hitbox_x = b_image.get_rect().size[0]
        self.hitbox_y = b_image.get_rect().size[0]


def load_image(name):
    image = pygame.image.load(name).convert_alpha()
    image = pygame.transform.scale(image, (int(image.get_rect().size[0] * 0.75), int(image.get_rect().size[1] * 0.75)))
    return image


#pygame.init()
display_width = 500
display_heigh = 680
window = pygame.display.set_mode((display_width, display_heigh))
pygame.display.set_caption('KittyMama')
gameDisplay = pygame.Surface((display_width, display_heigh))
surface = load_image('back.jpg')
surface = pygame.transform.scale(surface, (display_width, display_heigh))
window.blit(surface, (0, 0))
pygame.display.flip()

cat_list = pygame.sprite.Group()

cat1_img = load_image('cat1.png')
cat2_img = load_image('cat2.png')
cat3_img = load_image('cat3.png')
cat4_img = load_image('cat4.png')
basket_img = pygame.image.load('basket.png').convert_alpha()
basket_img = pygame.transform.scale(basket_img, (int(basket_img.get_rect().size[0] / 2),\
                                                 int(basket_img.get_rect().size[1] / 2)))

def basket(x, y):
    window.blit(basket_img, (x, y))


def score_counter(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score:" + str(count), True, black)
    gameDisplay.blit(text, (0, 0))


clock = pygame.time.Clock()


def game_loop():
    pygame.init()
    x = display_width / 2 - 50
    y = display_heigh - 259 / 2
    x_change = 0

    cat1 = Gameobject(cat1_img, 5, random.randint(int(97 / 2), display_width - 48), -random.randint(160, 500))
    cat2 = Gameobject(cat2_img, 3, random.randint(int(97 / 2), display_width - 48), -random.randint(160, 500))
    cat3 = Gameobject(cat3_img, 3, random.randint(int(97 / 2), display_width - 48), -random.randint(160, 500))
    cat4 = Gameobject(cat4_img, 4, random.randint(int(97 / 2), display_width - 48), -random.randint(160, 500))
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
                    if x < display_width - 213 / 2 - 3:
                        x_change = 4
                    else:
                        x_change = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        if 0 <= x <= display_width - 213 / 2:
            x += x_change

        window.blit(surface, (0, 0))

        window.blit(cat1.b_image, (cat1.coord_x, cat1.coord_y))
        window.blit(cat2.b_image, (cat2.coord_x, cat2.coord_y))
        window.blit(cat3.b_image, (cat3.coord_x, cat3.coord_y))
        window.blit(cat4.b_image, (cat4.coord_x, cat4.coord_y))
        print('1')
        basket(x, y)
        cat1.coord_y += cat1.speed
        cat2.coord_y += cat2.speed
        cat3.coord_y += cat2.speed
        cat4.coord_y += cat4.speed

        if cat1.coord_y > display_heigh:
            cat1.coord_y = -random.randint(160, 500)
            cat1.coord_x = random.randint(int(97 / 2), display_width - 48)
            cat1.speed = random.randint(3, 8)
        if cat2.coord_y > display_heigh - 10:
            cat2.coord_y = -random.randint(160, 500)
            cat2.coord_x = random.randint(int(97 / 2), display_width - 48)
            cat2.speed = random.randint(3, 8)
        if cat3.coord_y > display_heigh:
            cat3.coord_y = -random.randint(160, 500)
            cat3.coord_x = random.randint(int(97 / 2), display_width - 48)
            cat3.speed = random.randint(3, 8)
        if cat4.coord_y > display_heigh:
            cat4.coord_y = -random.randint(160, 500)
            cat4.coord_x = random.randint(int(97 / 2), display_width - 48)
            cat4.speed = random.randint(3, 8)


        if x < 0:
            x += 4
        elif x > display_width - 213 / 2:
            x -= 3

        pygame.display.update()
        clock.tick(60)
game_loop()
pygame.quit()
quit()
