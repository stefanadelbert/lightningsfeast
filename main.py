import sys
import random
import pygame

# Constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

BURGER_COUNT = 20
OBSTACLES_COUNT = 5
TREES_COUNT = 10

obstacle_images = ['resources/rocks1.png']
trees_images = ['resources/trees1.png', 'resources/trees2.png', 'resources/trees3.png', 'resources/trees4.png']

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

class Obstacle(Block):
    def __init__(self):
        image = obstacle_images[random.randint(1, len(obstacle_images)) - 1]
        super(Obstacle, self).__init__(image)

class Trees(Block):
    def __init__(self):
        image = trees_images[random.randint(1, len(trees_images)) - 1]
        super(Trees, self).__init__(image)

class Player(Block):
    def __init__(self):
        super(Player, self).__init__('resources/lightning.png')

pygame.init()
pygame.display.set_caption('Lighting\'s Feast')
screen = pygame.display.set_mode(screen_size)

hamburger_list = pygame.sprite.Group()
obstacle_list = pygame.sprite.Group()
trees_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

# Create Lightning and add him to the all sprites list.
player = Player()
all_sprites_list.add(player)

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

while len(obstacle_list) < OBSTACLES_COUNT:
    obstacle = Obstacle()

    obstacle.rect.x = random.randrange(screen_width - obstacle.rect.width)
    obstacle.rect.y = random.randrange(screen_height - obstacle.rect.height)

    if len(pygame.sprite.spritecollide(obstacle, all_sprites_list, False)):
        # If this sprite collides with another, then throw it away and try again.
        continue

    obstacle_list.add(obstacle)
    all_sprites_list.add(obstacle)

while len(trees_list) < TREES_COUNT:
    trees = Trees()

    trees.rect.x = random.randrange(screen_width - trees.rect.width)
    trees.rect.y = random.randrange(screen_height - trees.rect.height)

    trees_list.add(trees)
    all_sprites_list.add(trees)

# Initialise some main loop variables.
clock = pygame.time.Clock()
done = False
score = 0

# Render some text
score_label_font = pygame.font.SysFont('Ubuntu', 25, bold=True)

# Start the main loop and run it until done is True.
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(background_fill)

    pos = pygame.mouse.get_pos()

    player.rect.x = pos[0]
    player.rect.y = pos[1]

    obstacle_hit_list = pygame.sprite.spritecollide(
        player, obstacle_list, False, collided=pygame.sprite.collide_rect_ratio(0.8))
    if len(obstacle_hit_list):
        done = True
        continue

    hamburger_hit_list = pygame.sprite.spritecollide(player, hamburger_list, True)

    for block in hamburger_hit_list:
        score += 1

    if BURGER_COUNT == score:
        done = True

    all_sprites_list.draw(screen)

    score_label = score_label_font.render('Score {}'.format(score), True, BLACK)
    screen.blit(score_label, (screen.get_rect().width - score_label.get_rect().width - 10, 10))

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
