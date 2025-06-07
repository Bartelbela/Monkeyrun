# main.py

import pygame
import sys
from game import Game

def main():
    pygame.init()
    screen = pygame.display.set_mode((1920, 500))
    pygame.display.set_caption("Monkey Jump")
    game = Game(screen)
    game.run()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()