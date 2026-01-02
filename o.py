import pygame # type: ignore
from constants import RED, LINE_WIDTH, SQUARE_SIZE

class O(pygame.sprite.Sprite):
    def __init__(self):
        self.name = "Player O"
        self.letter = "o"
        self.radius = SQUARE_SIZE / 2

    def draw(self, screen, x, y):
        pygame.draw.circle(screen, RED, ((x + (SQUARE_SIZE / 2)), (y + (SQUARE_SIZE / 2))), self.radius, LINE_WIDTH)

    