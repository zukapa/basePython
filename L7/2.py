from abc import ABC, abstractmethod


class Dress(ABC):
    def __init__(self, name, parameter):
        self.dress_name = name
        self.dress_parameter = parameter
        self.coat = []
        self.result = []

    def __add__(self, other):
        if len(self.coat) == 0:
            self.coat.append(self.cloth_cost)
            self.coat.append(other.cloth_cost)
        else:
            self.coat.append(other.cloth_cost)
        return self

    @property
    def calculate(self):
        a = map(float, self.coat)
        return f'Общий расход ткани: {sum(a)}'

    @abstractmethod
    def cloth_cost(self):
        pass


class Coat(Dress):
    @property
    def cloth_cost(self):
        return str(self.dress_parameter / 6.5 + 0.5)


class Suit(Dress):
    @property
    def cloth_cost(self):
        return 2 * self.dress_parameter + 0.3


c = Coat('Пальто1', 50)
c1 = Coat('Пальто2', 60)
s = Suit('Костюм1', 171)
s1 = Suit('Костюм2', 180)
c + c1 + s + s1
print(f'Расход ткани: '
      f'{c.dress_name}: {c.cloth_cost}, '
      f'{s.dress_name}: {s.cloth_cost}, '
      f'{c1.dress_name}: {c1.cloth_cost}, '
      f'{s1.dress_name}: {s1.cloth_cost}')
print(c.calculate)
