import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 200, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.velocity = 0

    def update(self):
        self.rect.y += self.velocity