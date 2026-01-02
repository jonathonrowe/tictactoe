import pygame # type: ignore
from constants import *
from board import Board
from x import X
from o import O

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

    font = pygame.font.SysFont(FONT, FONT_SIZE, bold=False, italic=False)

    board = Board()
    current_player = "x"

    x = None
    y = None
    player_x = X()
    player_o = O()

    running = True
    while running:        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                x = pos[0]
                y = pos[1]

                if 0 <= y <= SQUARE_SIZE - 1:
                    clicked_row = 0
                elif SQUARE_SIZE <= y <= SQUARE_SIZE * 2 - 1:
                    clicked_row = 1
                elif SQUARE_SIZE * 2 <= y <= SQUARE_SIZE * 3:
                    clicked_row = 2

                if 0 <= x <= SQUARE_SIZE - 1:
                    clicked_col = 0
                elif SQUARE_SIZE <= x <= SQUARE_SIZE * 2 - 1:
                    clicked_col = 1
                elif SQUARE_SIZE * 2 <= x <= SQUARE_SIZE * 3:
                    clicked_col = 2       

                if board.board[clicked_row][clicked_col] is None:
                    if current_player == "x":
                        board.board[clicked_row][clicked_col] = "x"
                        current_player = "o"
                    elif current_player == "o":
                        board.board[clicked_row][clicked_col] = "o"
                        current_player = "x"
                
        screen.fill(WHITE)
        draw_lines(screen)

        for row in range(3):
            for col in range(3):
                content = board.board[row][col]

                screen_x = col * SQUARE_SIZE
                screen_y = row * SQUARE_SIZE

                if content == "x":
                    player_x.draw(screen, screen_x, screen_y)
                elif content == "o":
                    player_o.draw(screen, screen_x, screen_y)
        
        pygame.display.flip()

if __name__ == "__main__":
    main()
