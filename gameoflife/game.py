class GameOfLife:
    def __init__(self, rows, columns, livingCells=None):
        self.rows = rows
        self.columns = columns
        self.livingCells = livingCells

    @classmethod
    def load(cls, string_repr: str):
        lines = string_repr.split('\n')
        columns = len(lines[0].split(' '))
        living_cells = []
        y = -1
        for line in lines:
            y += 1
            x = -1
            points = line.split(' ')
            for point in points:
                x += 1
                if point == '*':
                    living_cells.append(Point(x, y))

        return GameOfLife(len(lines), columns, living_cells)

    def getNextGeneration(self):
        next_gen_cells=[]


        return GameOfLife(self.rows, self.columns, next_gen_cells)

    def __str__(self):
        return "."


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
