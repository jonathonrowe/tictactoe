import pygame # type: ignore
from constants import SQUARE_SIZE

class Board():
    def __init__(self):
        self.board = [
            [], [], [],
            [], [], [],
            [], [], []
        ]

