from cell import Cell

class SquareGrid:
    def __init__(self, size):
        self.size = size
        self.cells = [[Cell() for _ in range(size)] for _ in range(size)]

    def get_cell(self, row, col):
        return self.cells[row][col]
