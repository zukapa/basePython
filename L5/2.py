with open('small_text.txt', 'r', encoding='utf=8') as my_file:
    lines = 0
    for line in my_file:
        lines += 1
        num_words = line.split()
        print(f'{line.strip()} - {len(num_words)} сл.')
    print(f'Всего {lines} строки')
