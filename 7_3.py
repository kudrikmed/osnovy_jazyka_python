class Cell:
    def __init__(self, cellulas):
        self.cellulas = cellulas

    def __add__(self, other):
        return Cell(self.cellulas + other.cellulas)

    def __sub__(self, other):
        if self.cellulas > other.cellulas:
            return Cell(self.cellulas - other.cellulas)
        else:
            return "Your cell is too small"

    def __mul__(self, other):
        return Cell(self.cellulas * other.cellulas)

    def __truediv__(self, other):
        return Cell(self.cellulas // other.cellulas)

    def make_order(self, rows):
        stars = self.cellulas
        output = ""
        for _ in range(stars // rows):
            output += "*" * rows + "\n"
        output += "*" * (stars % rows)
        return output


cell_1 = Cell(14)
cell_2 = Cell(3)
cell_3 = cell_1 / cell_2
print(cell_3.make_order(10))
