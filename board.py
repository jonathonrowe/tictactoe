import pygame # type: ignore
from constants import SQUARE_SIZE

class Board():
    def __init__(self):
        self.board = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]

    def check_winner(self, player):
        for i in range(3):
            if self.board[i][0] == player.letter and self.board[i][1] == player.letter and self.board[i][2] == player.letter:
                return True
        for i in range(3):
            if self.board[0][i] == player.letter and self.board[1][i] == player.letter and self.board[2][i] == player.letter:
                return True
        if self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player:
            return True
        if self.board[2][0] == player and self.board[1][1] == player and self.board[0][2] == player:
            return True

    def check_draw(self):
        return all(all(cell is not None for cell in row) for row in self.board)