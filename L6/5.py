class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        return f'Запуск отрисовки объекта - {self.title}'


class Pencil(Stationery):
    def draw(self):
        return f'Запуск отрисовки объекта - {self.title}'


class Handle(Stationery):
    def draw(self):
        return f'Запуск отрисовки объекта - {self.title}'


mess1 = Pen('ручка')
mess2 = Pencil('карандаш')
mess3 = Handle('маркер')
print(mess1.draw())
print(mess2.draw())
print(mess3.draw())