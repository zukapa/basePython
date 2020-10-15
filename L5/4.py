my_dict = {'One': 'Один',
           'Two': 'Два',
           'Three': 'Три',
           'Four': 'Четыре'}
new = []
with open('numeral.txt', 'r', encoding="utf=8") as my_f:
    for line in my_f:
        num = line.split()
        new.append(f'{my_dict[num[0]]} - {num[2]} \n')
        print(line.strip())
    print(new)
with open('new_numeral.txt', 'w', encoding="utf =8") as my_f1:
    my_f1.writelines(new)
