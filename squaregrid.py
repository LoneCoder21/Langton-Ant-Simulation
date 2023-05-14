from cell import Cell

class SquareGrid:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[Cell() for _ in range(h)] for _ in range(w)]

    def get_cell(self, col, row):
        return self.cells[col][row]
