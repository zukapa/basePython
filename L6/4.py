class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.color} {self.name} поехал'

    def stop(self):
        return f'остановился'

    def turn(self, direction):
        if direction == 'направо':
            return f'повернул {direction}'
        else:
            return f'повернул {direction}'

    def show_speed(self):
        return f'скорость - {self.speed}'

    def show_is_police(self):
        if self.is_police is True:
            return f'Полицейский автомобиль'
        else:
            return f''


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'скорость - {self.speed} (превышение скорости!)'
        else:
            return f'скорость - {self.speed}'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'скорость - {self.speed} (превышение скорости!)'
        else:
            return f'скорость - {self.speed}'


class PoliceCar(Car):
    pass


car1 = TownCar(70, 'Красный', 'BMW', False)
print(f'{car1.go()}, {car1.show_speed()}, {car1.turn("налево")} и {car1.stop()}. {car1.show_is_police()}')

car2 = SportCar(150, 'Зеленый', 'Ferrari', False)
print(f'{car2.go()}, {car2.show_speed()}, {car2.turn("направо")} и {car2.stop()}. {car2.show_is_police()}')

car3 = WorkCar(35, 'Синий', 'Lada', False)
print(f'{car3.go()}, {car3.show_speed()}, {car3.turn("налево")} и {car3.stop()}. {car3.show_is_police()}')

car4 = WorkCar(95, 'Желтый', 'VAZ', False)
print(f'{car4.go()}, {car4.show_speed()}, {car4.turn("направо")} и {car4.stop()}. {car4.show_is_police()}')

car5 = PoliceCar(80, 'Бело-синий', 'Volkswagen', True)
print(f'{car5.go()}, {car5.show_speed()}, {car5.turn("налево")} и {car5.stop()}. {car5.show_is_police()}')
