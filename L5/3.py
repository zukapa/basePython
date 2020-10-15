with open('wage-worker.txt', 'r', encoding='utf=8') as my_f:
    aggregate = []
    lines = 0
    for line in my_f:
        lines += 1
        work = line.split()
        aggregate.append(int(work[1]))
        if int(work[1]) < 20000:
            print(f'{work[0]}: оклад меньше 20000')
    average_wage = (sum(aggregate)) / lines
    print(f'Средняя величина дохода сотрудника составляет {average_wage}')
