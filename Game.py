import pygame, random, os


class Gameobject(pygame.sprite.Sprite):
    def __init__(self, image, speed, coord_x, coord_y):
        super().__init__()
        self.image = image
        self.speed = speed
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = coord_x
        self.rect.y = coord_y


def load_image(name):
    image = pygame.image.load(name).convert_alpha()
    image = pygame.transform.scale(image, (int(image.get_rect().size[0] * 0.75), int(image.get_rect().size[1] * 0.75)))
    return image

pygame.init()
display_width = 500
display_heigh = 680
window = pygame.display.set_mode((display_width, display_heigh))
pygame.display.set_caption('KittyMama')
gameDisplay = pygame.Surface((display_width, display_heigh))
surface = load_image('back.jpg')
surface = pygame.transform.scale(surface, (display_width, display_heigh))
window.blit(surface, (0, 0))
pygame.display.flip()

cat1_img = load_image('cat1.png')
cat2_img = load_image('cat2.png')
cat3_img = load_image('cat3.png')
cat4_img = load_image('cat4.png')
cats_img = [cat1_img, cat2_img, cat3_img, cat4_img]

basket_img = pygame.image.load('basket.png').convert_alpha()
basket_img = pygame.transform.scale(basket_img, (int(basket_img.get_rect().size[0] / 2), \
                                                 int(basket_img.get_rect().size[1] / 2)))


def score_counter(count):
    font = pygame.font.SysFont("comicsansms", 35)
    text = font.render("Score:" + str(count), True, (84, 197, 222))
    window.blit(text, (330, 70))


clock = pygame.time.Clock()


def game_loop():
    cat_list = pygame.sprite.Group()
    x_change = 0
    score = 0

    basket = Gameobject(basket_img, 4, display_width / 2 - 50, display_heigh - 259 / 2)
    basket_collide_mask = pygame.image.load('basket_collide_mask.png')
    basket_collide_mask = pygame.transform.scale(basket_collide_mask, (int(basket_collide_mask.get_rect().size[0] / 2), \
                                        int(basket_collide_mask.get_rect().size[1] / 2)))
    basket.mask = basket.mask.clear()
    basket.mask = pygame.mask.from_surface(basket_collide_mask)
    for i in [0, 1, 2, 3]:
        cat = Gameobject(cats_img[i], random.randint(3, 6), random.randint(int(97 / 2), display_width - 48),
                         -random.randint(160, 500))
        cat_list.add(cat)

    end = False
    start_ticks = pygame.time.get_ticks()
    while not end:
        seconds = (pygame.time.get_ticks() - start_ticks) / 1000
        if seconds > 100:
            end = True
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if basket.rect.x > 3:
                        x_change = -4
                    else:
                        x_change = 0
                elif event.key == pygame.K_RIGHT:
                    if basket.rect.x < display_width - 213 / 2 - 3:
                        x_change = 4
                    else:
                        x_change = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        if 0 <= basket.rect.x <= display_width - 213 / 2:
            basket.rect.x += x_change

        window.blit(surface, (0, 0))
        score_counter(score)
        cat_hit_list = pygame.sprite.spritecollide(basket, cat_list, True, pygame.sprite.collide_mask)

        cat_list.draw(window)

        window.blit(basket_img, (basket.rect.x, basket.rect.y))

        for cat in cat_list:
            cat.rect.y += cat.speed
            if cat.rect.y > display_heigh:
                cat.rect.y = -random.randint(160, 500)
                cat.rect.x = random.randint(int(97 / 2), display_width - 48)
                cat.speed = random.randint(3, 6)

        for cat in cat_hit_list:
            score += 1
            c = random.randint(0, 3)
            cat = Gameobject(cats_img[c], random.randint(3, 6), random.randint(int(97 / 2), display_width - 48), \
                             -random.randint(160, 500))
            cat_list.add(cat)


        if basket.rect.x < 0:
            basket.rect.x += 4
        elif basket.rect.x > display_width - 213 / 2:
            basket.rect.x -= 3

        pygame.display.update()
        clock.tick(70)


game_loop()
pygame.quit()
quit()
