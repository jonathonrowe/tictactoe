import pygame # type: ignore
from constants import BLUE, LINE_WIDTH, SQUARE_SIZE

class X(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, screen, x, y):
        pygame.draw.line(screen, BLUE, (x, y), (x + SQUARE_SIZE, y + SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, BLUE, (x, y + SQUARE_SIZE), (x + SQUARE_SIZE, y), LINE_WIDTH)
