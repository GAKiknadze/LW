try:
    g = input('Введите пол кандидата(м/ж): ')
    a = int(input('Введите возраст кандидата:'))
    if g == 'м' and a>=18 and a<=35:
        print('Подходит')
    else:
        print('Не подходит')
except ValueError:
    print('Ошибка ввода.')