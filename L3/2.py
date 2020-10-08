def my_func(name, surname, year, city, email, tel_number):
    return ' '.join([name, surname, year, city, email, tel_number])


print(my_func(surname=input('фамилия: '), name=input('имя: '),
              year=input('год рождения: '), city=input('город: '),
              email=input('эл.почта: '), tel_number=input('телефон: ')))
