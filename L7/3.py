class Cell:
    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        return f'размер клетки при сложении {self.quantity + other.quantity}'

    def __sub__(self, other):
        sub = self.quantity - other.quantity
        if sub > 0:
            return f'размер клетки при вычитании {sub}'
        else:
            return f'вычитание не выполнимо, результат < 0'

    def __mul__(self, other):
        return f'размер клетки при произвидении {self.quantity * other.quantity}'

    def __truediv__(self, other):
        return f'размер клетки при делении {self.quantity // other.quantity}'

    def make_order(self, unit):
        row = '*' * unit + '/n'
        rest = '*' * (self.quantity % unit)
        str_row = row * (self.quantity // unit) + rest
        return str_row


a = Cell(28)
b = Cell(10)
c = Cell(200)
print(f'{a + b}\n{a - c}\n{a - b}\n{a * b}\n{a / b}\n{a.make_order(5)}')
