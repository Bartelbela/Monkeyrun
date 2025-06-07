import pygame

class UI:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)

    def draw_score(self, score):
        text = self.font.render(f"Punkte: {score}", True, (255, 255, 255))
        self.screen.blit(text, (10, 10))