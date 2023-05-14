from cell import Cell

class SquareGrid:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.grid = [[Cell() for _ in range(h)] for _ in range(w)]

    def getCell(self, col, row):
        return self.grid[col][row]
