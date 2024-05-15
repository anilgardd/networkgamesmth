import pygame

class Spaceship(pygame.sprite.Sprite):
    def __init__(self, x, y, health, color, id):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/spaceship.png")
        self.image.fill(color)  # Color the spaceship
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.health_start = health
        self.health_remaining = health
        self.last_shot = pygame.time.get_ticks()
        self.id = id
        self.vel = 8

    def draw(self, win):
        win.blit(self.image, self.rect.topleft)
        pygame.draw.rect(win, (255, 0, 0), (self.rect.x, self.rect.bottom + 10, self.rect.width, 15))
        if self.health_remaining > 0:
            pygame.draw.rect(win, (0, 255, 0), (self.rect.x, self.rect.bottom + 10, int(self.rect.width * (self.health_remaining / self.health_start)), 15))

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.vel
        if keys[pygame.K_RIGHT] and self.rect.right < 600:  # screen_width
            self.rect.x += self.vel

        self.update()

    def update(self):
        self.rect = (self.rect.x, self.rect.y, self.rect.width, self.rect.height)
