try:
    m = int(input('Введите номер месяца: '))
    if m == 1 or m == 2 or m == 12:
        t = 'зима'
    elif m > 2 and m <= 5:
        t = 'весна'
    elif m >5 and m <=8:
        t = 'лето'
    elif m > 8 and m <= 11:
        t = 'осень'
    else:
        print('Нет такого месяца.')
        quit()
    print('Время года:',t)

except ValueError:
    print('Ошибка ввода.')