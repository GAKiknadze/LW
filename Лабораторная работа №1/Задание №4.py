import math
try:
    x1,y1 = input('Введите координаты первой точки: ').split()
    x2,y2 = input('Введите координаты второй точки: ').split()
    x1 = float(x1) ; x2 = float(x2) ; y1 = float(y1) ; y2 = float(y2)
    if x1 == x2 and y1 == y2:
        raise Exception
    print('Длина отрезка: ',math.sqrt((x2-x1)**2+(y2-y1)**2))
except (ValueError,Exception):
    print('Ошибка ввода!!!')