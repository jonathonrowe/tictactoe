import pygame # type: ignore
from constants import *

def draw_lines(display):
    # Horizontal lines
    pygame.draw.line(display, BLACK, (0, SQUARE_SIZE), (SCREEN_WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(display, BLACK, (0, SQUARE_SIZE * 2), (SCREEN_WIDTH, SQUARE_SIZE * 2), LINE_WIDTH)

    # Vertical lines
    pygame.draw.line(display, BLACK, (SQUARE_SIZE, 0), (SQUARE_SIZE, SCREEN_HEIGHT), LINE_WIDTH)
    pygame.draw.line(display, BLACK, (SQUARE_SIZE * 2, 0), (SQUARE_SIZE * 2, SCREEN_HEIGHT), LINE_WIDTH)

def main():
    print("You are playing Tic Tac Toe")
    pygame.init()    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Tic Tac Toe by Jon")

    clock = pygame.time.Clock()
    dt = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)
        draw_lines(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main()
