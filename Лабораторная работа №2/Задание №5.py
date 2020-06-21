try:
    x = []
    k = 1
    print('Введите три числа:')
    for i in range(1,4):
        x.append(float(input('1: ')))
    for  i in range(3):
        k = x.count(x[i])
    if k >= 2:
        print('Количество одинаковых чисел:', k)
    else:
        print('Нет одинаковых чтсел.')
except ValueError:
    print('Ошибка ввода.')