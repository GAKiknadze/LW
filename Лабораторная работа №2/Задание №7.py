try:
    r =float(input('Введите радиус окружности: '))
    x,y = map(float,input('Введите координаты точки в формате(X,Y): ').split())
    if (x>=0 and x*x + y*y <= r*r)or(x>=-r and y<=r and y>=-r and (x>=y or y>=-x)):
        print('Точка находится в закрашенной области.')
    else:
        print('Число не попадает в область.')
except ValueError:
    print('Ошибка ввода')