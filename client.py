import pygame
from network import Network
from spaceship import Spaceship
from aliens import Aliens, Alien_Bullets

pygame.init()

# Define screen dimensions and create a window
screen_width = 600
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Space Invaders')

# Define colors
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)

# Load images and sounds
bg = pygame.image.load("img/bg.png")
explosion_fx = pygame.mixer.Sound("sounds/explosion.wav")
explosion_fx.set_volume(0.25)
laser_fx = pygame.mixer.Sound("sounds/laser.wav")
laser_fx.set_volume(0.25)

# Define fonts
font30 = pygame.font.SysFont('Constantia', 30)
font40 = pygame.font.SysFont('Constantia', 40)

# Define clock for FPS
clock = pygame.time.Clock()
fps = 60

# Create sprite groups
spaceship_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
alien_group = pygame.sprite.Group()
alien_bullet_group = pygame.sprite.Group()
explosion_group = pygame.sprite.Group()

# Create spaceship
def create_spaceship(id):
    color = (0, 255, 0) if id == 0 else (255, 0, 0)
    spaceship = Spaceship(int(screen_width / 2), screen_height - 100, 3, color, id)
    spaceship_group.add(spaceship)
    return spaceship

# Create aliens
def create_aliens():
    rows = 5
    cols = 5
    for row in range(rows):
        for item in range(cols):
            alien = Aliens(100 + item * 100, 100 + row * 70)
            alien_group.add(alien)

create_aliens()

# Main game loop
def main():
    run = True
    n = Network()
    player = create_spaceship(n.getP())
    clock = pygame.time.Clock()

    while run:
        clock.tick(fps)
        screen.fill((0, 0, 0))
        screen.blit(bg, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        keys = pygame.key.get_pressed()
        player.move(keys)

        # Send player data to server and receive updated data
        player_data = n.send(player)
        if player_data:
            player.rect.x = player_data.x
            player.rect.y = player_data.y

        # Update all sprite groups
        spaceship_group.update()
        bullet_group.update()
        alien_group.update()
        alien_bullet_group.update()
        explosion_group.update()

        # Draw all sprite groups
        spaceship_group.draw(screen)
        bullet_group.draw(screen)
        alien_group.draw(screen)
        alien_bullet_group.draw(screen)
        explosion_group.draw(screen)

        # Update display
        pygame.display.update()

main()
