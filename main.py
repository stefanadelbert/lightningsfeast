import sys
import random
import pygame

# Constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

BURGER_COUNT = 20
ROCKS_COUNT = 5
TREES_COUNT = 10

screen_size = screen_width, screen_height = 700, 400

background_fill = WHITE

class Block(pygame.sprite.Sprite):
    def __init__(self, image):
        super(Block, self).__init__()

        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()

class Hamburger(Block):
    def __init__(self):
        super(Hamburger, self).__init__('resources/hamburger.png')

class Rocks(Block):
    def __init__(self):
        super(Rocks, self).__init__('resources/rocks1.png')

class Trees(Block):
    def __init__(self):
        super(Trees, self).__init__('resources/trees1.png')

class Player(Block):
    def __init__(self):
        super(Player, self).__init__('resources/lightning.png')

pygame.init()
pygame.display.set_caption('Lighting\'s Feast')
screen = pygame.display.set_mode(screen_size)

hamburger_list = pygame.sprite.Group()
rocks_list = pygame.sprite.Group()
trees_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

# Create burgers for Lightning to eat and add them to the all sprites list and
# the burgers list.
while len(hamburger_list) < BURGER_COUNT:
    hamburger = Hamburger()

    hamburger.rect.x = random.randrange(screen_width - hamburger.rect.width)
    hamburger.rect.y = random.randrange(screen_height - hamburger.rect.height)

    if len(pygame.sprite.spritecollide(hamburger, all_sprites_list, False)):
        # If this sprite collides with another, then throw it away and try again.
        continue

    hamburger_list.add(hamburger)
    all_sprites_list.add(hamburger)

while len(rocks_list) < ROCKS_COUNT:
    rocks = Rocks()

    rocks.rect.x = random.randrange(screen_width - rocks.rect.width)
    rocks.rect.y = random.randrange(screen_height - rocks.rect.height)

    if len(pygame.sprite.spritecollide(rocks, all_sprites_list, False)):
        # If this sprite collides with another, then throw it away and try again.
        continue

    rocks_list.add(rocks)
    all_sprites_list.add(rocks)

while len(trees_list) < TREES_COUNT:
    trees = Trees()

    trees.rect.x = random.randrange(screen_width - trees.rect.width)
    trees.rect.y = random.randrange(screen_height - trees.rect.height)

    trees_list.add(trees)
    all_sprites_list.add(trees)

# Create Lightning and add him to the all sprites list.
player = Player()
all_sprites_list.add(player)

# Initialise some main loop variables.
clock = pygame.time.Clock()
done = False
score = 0

# Render some text
score_label_font = pygame.font.SysFont('Ubuntu', 20, bold=True)

# Start the main loop and run it until done is True.
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(background_fill)

    pos = pygame.mouse.get_pos()

    player.rect.x = pos[0]
    player.rect.y = pos[1]

    rocks_hit_list = pygame.sprite.spritecollide(player, rocks_list, False)
    if len(rocks_hit_list):
        done = True
        continue

    hamburger_hit_list = pygame.sprite.spritecollide(player, hamburger_list, True)

    for block in hamburger_hit_list:
        score += 1

    score_label = score_label_font.render('Score {}'.format(score), True, BLACK)
    screen.blit(score_label, (1, 10))

    if BURGER_COUNT == score:
        done = True

    all_sprites_list.draw(screen)

    pygame.display.flip()

    clock.tick(60)

# End of game sequence.
game_message_font = pygame.font.SysFont('Ubuntu', 30, bold=True)
if BURGER_COUNT == score:
    end_message = game_message_font.render('Victory', True, BLACK)
else:
    end_message = game_message_font.render('Game Over', True, BLACK)

text_rect = end_message.get_rect()
text_rect.centerx = screen.get_rect().centerx
text_rect.centery = screen.get_rect().centery
screen.blit(end_message, text_rect)
pygame.display.flip()

# Delay for 3 seconds
pygame.time.delay(3000)

pygame.quit()
