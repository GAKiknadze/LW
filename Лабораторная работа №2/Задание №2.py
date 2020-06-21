try:
    x = []
    print('Введите пять чисел:')
    for i in range(1,6):
        x.append(float(input('1: ')))
    print('Min:',min(x))
    print('Max:',max(x))
except ValueError:
    print('Ошибка ввода.')