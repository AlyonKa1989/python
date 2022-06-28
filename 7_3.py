# f = open("7_3.txt", "w", encoding="utf-8") - условие задачи
# f.close()

class Cell:

    def __init__(self, count):
        self.count = int(count)

    def make_order(self, rows):
        return '\n'.join(['__' * rows for _ in range(self.count // rows)]) + '\n' + '^^' * (self.count % rows)

    def __str__(self):
        return f"{self.count}"

    def __add__(self, other):
        print("Сумма ячеек: ")
        return Cell(self.count + other.count)

    def __sub__(self, other):
        print("Результат вычитания ячеек: ")
        return Cell(self.count - other.count) if self.count - other.count > 0 \
            else "Вычесть невозможно, ячеек в первой клетке меньше, чем во второй"

    def __mull__(self, other):
        print("Резульат умножения ячеек: ")
        return Cell(self.count * other.count)

    def __truediv__(self, other):
        print("Результат деления ячеек: ")
        return Cell(self.count // other.count)


cell_1 = Cell(333)
cell_2 = Cell(33)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
#print(cell_1 * cell_2)
#print(cell_1 // cell_2)
print(cell_2.make_order(7))
