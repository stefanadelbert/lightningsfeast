import sys
import random
import pygame

# Constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

screen_size = screen_width, screen_height = 700, 400

background_fill = WHITE

class Block(pygame.sprite.Sprite):
    def __init__(self, image):
        super(Block, self).__init__()

        self.image = pygame.image.load(image).convert()
        self.rect = self.image.get_rect()

class Hamburger(Block):
    def __init__(self):
        super(Hamburger, self).__init__('resources/hamburger.png')

class Player(Block):
    def __init__(self):
        super(Player, self).__init__('resources/lightning.png')

pygame.init()
screen = pygame.display.set_mode(screen_size)

hamburger_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

for i in range(50):
    hamburger = Hamburger()

    hamburger.rect.x = random.randrange(screen_width)
    hamburger.rect.y = random.randrange(screen_height)

    hamburger_list.add(hamburger)
    all_sprites_list.add(hamburger)

player = Player()
all_sprites_list.add(player)

done = False

clock = pygame.time.Clock()

score = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(background_fill)

    pos = pygame.mouse.get_pos()

    player.rect.x = pos[0]
    player.rect.y = pos[1]

    hamburger_hit_list = pygame.sprite.spritecollide(player, hamburger_list, True)

    for block in hamburger_hit_list:
        score += 1
        print(score)

    all_sprites_list.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
