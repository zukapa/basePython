my_dict = {}
with open('study.txt', 'r', encoding="utf=8") as my_f:
    for line in my_f:
        name, lecture, practice, laboratory = line.split()
        if lecture == '-':
            lecture = 0
        else:
            lecture = (int(lecture[:-3]))
        if practice == '-':
            practice = 0
        else:
            practice = (int(practice[:-4]))
        if laboratory == '-':
            laboratory = 0
        else:
            laboratory = (int(laboratory[:-5]))
        my_sum = lecture + practice + laboratory
        my_dict[name[:-1]] = my_sum
print(f'Общее количество часов по предмету : {my_dict}')
