import math
import random
S = 0
P = 1
print('Введите четыре двузначных числа:')
for i in range(4):
    try:
        a = input('{}: '.format(i+1))
        a = int(a)
        if (a//10 > 0 and a//10 <= 9) or (a//10 >= -9 and a//10 <= -1) :
           S += a
           P *= a
        else:
            raise Exception()
    except (ValueError,Exception):
        print('Ошибка ввода!!!')
        quit()
print('''Сумма: {}
Произведение: {}
Среднее арифметическое: {}
'''.format(S,P,S/4)
)
