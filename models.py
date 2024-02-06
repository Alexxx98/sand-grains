from settings import WHITE, BLACK


class Node:
    def __init__(self, row, col, width, height):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * height
        self.width = width
        self.height = height
        self.grain = BLACK

    def get_pos(self):
        return (self.row, self.col)

    def make_sand(self):
        self.grain = WHITE

    def make_space(self):
        self.grain = BLACK

    def is_sand(self):
        return self.grain == WHITE
