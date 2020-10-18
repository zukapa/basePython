class Road:
    def __init__(self, length, width, deep):
        self._length = length
        self._width = width
        self._deep = deep
        self.mass_asphalt()

    def mass_asphalt(self):
        return self._length * self._width * (self._deep * 5) * self._deep


r = Road(20, 5000, 5)
print(f'{r.mass_asphalt()} кг')