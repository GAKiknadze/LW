try:
    h,m = map(int,input('Введите время: ').split())
    if h > 24 or m > 60:
        h %= 24
        h += m//60
        m %= 60

    if h >= 0 and h<6 :
        t = 'ночь'
    elif h >= 6 and h < 12:
        t = 'утро'
    elif h >= 12 and h < 18:
        t = 'день'
    elif h >= 18 and h < 24:
        t = 'вечер'
    print('Текущее время [{}:{}]'.format(h,m))
    print('Время суток:',t)
except ValueError:
    print('Ошибка ввода.')