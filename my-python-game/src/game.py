import pygame

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.running = True

    def run(self):
        clock = pygame.time.Clock()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((135, 206, 235))  # Himmelblau
            pygame.display.flip()
            clock.tick(60)