import time
from itertools import cycle


class TrafficLight:
    def __init__(self):
        self.__color = cycle(['Красный', 'Желтый', 'Зеленый'])
        self.__time = [7, 2, 5]

    def running(self):
        for i in cycle(self.__time):
            print(next(self.__color))
            time.sleep(i)


tr = TrafficLight()
tr.running()
