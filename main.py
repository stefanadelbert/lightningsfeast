import sys
import random
import pygame

# Constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

BURGER_COUNT = 20

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
pygame.display.set_caption('Lighting\'s Feast')
screen = pygame.display.set_mode(screen_size)

hamburger_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

# Create burgers for Lightning to eat and add them to the all sprites list and
# the burgers list.
for i in range(BURGER_COUNT):
    hamburger = Hamburger()

    hamburger.rect.x = random.randrange(screen_width)
    hamburger.rect.y = random.randrange(screen_height)

    # Check that the hamburger is within the 
    while not screen.get_rect().contains(hamburger.rect):
        hamburger.rect.x = random.randrange(screen_width)
        hamburger.rect.y = random.randrange(screen_height)

    hamburger_list.add(hamburger)
    all_sprites_list.add(hamburger)

# Create Lightning and add him to the all sprites list.
player = Player()
all_sprites_list.add(player)

# Initialise some main loop variables.
clock = pygame.time.Clock()
done = False
score = 0

# Render some text
score_label_font = pygame.font.SysFont('Ubuntu', 20, bold=True)
game_message_font = pygame.font.SysFont('Ubuntu', 30, bold=True)

# Start the main loop and run it until done is True.
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(background_fill)
    score_label = score_label_font.render('Score {}'.format(score), True, BLACK)
    screen.blit(score_label, (1, 10))

    pos = pygame.mouse.get_pos()

    player.rect.x = pos[0]
    player.rect.y = pos[1]

    hamburger_hit_list = pygame.sprite.spritecollide(player, hamburger_list, True)

    for block in hamburger_hit_list:
        score += 1
        print(score)

    if BURGER_COUNT == score:
        done = True

    all_sprites_list.draw(screen)

    pygame.display.flip()

    clock.tick(60)

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
