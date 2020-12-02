import random


class Lotto:
    def __init__(self):
        self.tub = [i for i in range(1, 91)]
        self.win_computer = 0
        self.win_user = 0
        self.end = 0

    def gen_tub(self):
        if len(self.tub) < 30:
            return random.sample(self.tub, k=len(self.tub))
        else:
            return random.sample(self.tub, k=30)

    @staticmethod
    def sort_card(card):
        new_sort = sorted(card)
        card.clear()
        [card.append(i) for i in new_sort]
        [card.insert(random.randint(0, 4), ' ') for i, v in enumerate(card.copy()) if i < 4]

    def card(self):
        id_index = [1, 2, 3, 6, 7, 8]
        card_interface = [['-------Ваша карточка-------'],
                          [],
                          [],
                          [],
                          ['---------------------------'],
                          ['----Карточка компьютера----'],
                          [],
                          [],
                          [],
                          ['---------------------------']]
        for i, v in enumerate(self.gen_tub(), 1):
            if i <= 5:
                card_interface[1].append(v)
            elif (i > 5) and (i <= 10):
                card_interface[2].append(v)
            elif (i > 10) and (i <= 15):
                card_interface[3].append(v)
            elif (i > 15) and (i <= 20):
                card_interface[6].append(v)
            elif (i > 20) and (i <= 25):
                card_interface[7].append(v)
            elif (i > 25) and (i <= 30):
                card_interface[8].append(v)
        [self.sort_card(card_interface[i]) for i in id_index]
        while True:
            str_card = ''
            for i, v in enumerate(card_interface):
                for index, val in enumerate(v):
                    if len(str(val)) == 1 and str(val) != ' ':
                        str_card += ' ' + str(val) + ' '
                    elif len(str(val)) <= 2 and str(val) != ' ':
                        str_card += str(val) + ' '
                    elif str(val) == ' ':
                        str_card += '   '
                    else:
                        str_card += str(val)
                str_card += '\n'
            print(str_card)
            rand_tub = random.sample(self.tub, k=1)
            self.tub.remove(rand_tub[0])
            print(f'Бочонок номер: {rand_tub[0]}. Бочонков осталось: {len(self.tub)}')
            user_answer = input('Зачеркнуть цифру? (д, н): ')
            self.end = 0
            if user_answer == 'д':
                for i, v in enumerate(card_interface):
                    if 0 < i < 3:
                        for index, val in enumerate(v):
                            if val == rand_tub[0]:
                                v.remove(val)
                                v.insert(index, ' - ')
                                self.end = 2
                                self.win_user += 1
                            if self.win_user == 15:
                                print('Пользователь победил!')
                                self.end = 1
                                break
                        if self.end == 2 or self.end == 1:
                            break
                    if self.end == 2 or self.end == 1:
                        break
                    elif i == 3:
                        for index, val in enumerate(v):
                            if val == rand_tub[0]:
                                v.remove(val)
                                v.insert(index, ' - ')
                                self.end = 2
                                self.win_user += 1
                            if self.win_user == 15:
                                print('Пользователь победил!')
                                self.end = 1
                                break
                            if index == (len(v) - 1) and self.end == 0:
                                print('Игра окончена. Такого числа на карточке не было.')
                                self.end = 1
                                break
                        if self.end == 1:
                            break
                if self.end == 1:
                    break
            if user_answer == 'н':
                for i, v in enumerate(card_interface):
                    if 0 < i < 3:
                        for index, val in enumerate(v):
                            if val == rand_tub[0]:
                                print('Игра окончена. Такое число на карточке было.')
                                self.end = 1
                                break
                    elif i == 3:
                        for index, val in enumerate(v):
                            if val == rand_tub[0]:
                                print('Игра окончена. Такое число на карточке было.')
                                self.end = 1
                                break
                            if index == (len(v) - 1) and self.end == 0:
                                print('Продолжаем. Такого числа на карточке не было.')
                if self.end == 1:
                    break
            for i, v in enumerate(card_interface):
                if 5 < i < 9:
                    for index, val in enumerate(v):
                        if val == rand_tub[0]:
                            v.remove(val)
                            v.insert(index, ' - ')
                            self.win_computer += 1
                        if self.win_computer == 15:
                            print('Компьютер победил!')
                            self.end = 3
                            break
                    if self.end == 3:
                        break
            if self.end == 3:
                break


g = Lotto()
g.card()
