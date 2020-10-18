with open('my_text_file.txt', 'w', encoding='utf-8') as my_t_f:
    while True:
        my_str = input('Введите строку (пустая строка для завершения): ')
        if my_str == '':
            break
        my_t_f.write(my_str + '\n')
