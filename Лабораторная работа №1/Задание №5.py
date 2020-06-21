
from random import randint
try:
    choose = input('Хотите ввести трехзначное число вручную (y/n): ')
    if choose == 'y' or choose == 'Y':
        n = int(input('Введите число: '))
        if n //100 < 0 and n//100 > 10:
            raise Exception
        for i in str(n):
            print(i, end=' ')
    elif choose == 'n' or choose == 'N':
         n = randint(100,999)
         for i in str(n):
             print(i, end=' ')
    else:
        raise Exception
except (ValueError, Exception):
    print('Ошибка ввода!!!')