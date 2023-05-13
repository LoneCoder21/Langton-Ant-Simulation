from cell import Cell


class SquareGrid:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[Cell() for _ in range(w)] for _ in range(h)]

    def get_cell(self, row, col):
        return self.cells[row][col]
