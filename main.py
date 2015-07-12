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
    def __init__(self, colour, width, height):
        super(Block, self).__init__()

        self.image = pygame.Surface((width, height))
        self.image.fill(colour)

        self.rect = self.image.get_rect()

pygame.init()
screen = pygame.display.set_mode(screen_size)

block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

for i in range(50):
    block = Block(BLACK, 20, 15)

    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)

    block_list.add(block)
    all_sprites_list.add(block)

player = Block(RED, 20, 15)
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

    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)

    for block in blocks_hit_list:
        score += 1
        print(score)

    all_sprites_list.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
