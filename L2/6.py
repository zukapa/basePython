product = []
my_analit = {'название': [],
             'цена': [],
             'количество': [],
             'ед': []}
n = 0
while True:
    ex = input("ХАРАКТИРИСТИКА ТОВАРА. для продолжения нажмите enter, для выхода нажмите Q ")
    if ex == 'Q':
        break
    n += 1
    char = dict(название=input("введите название: "), цена=input('введите цену: '),
                количество=input('введите количество: '), ед=input('введите единицу измерения: '))
    product.append(tuple([n, char]))
    my_analit['название'].append(char['название'])
    my_analit['цена'].append(char['цена'])
    my_analit['количество'].append(char['количество'])
    my_analit['ед'].append(char['ед'])
print(product)
print(my_analit)
