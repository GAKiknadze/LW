try:
    k = input('Введите число: ')
    n = int(k)
    l = len(k)//2
    if n%2 == 0:
        print('Число четное.')
    else:
        print('Число не четное.')

    for i in range(l):
        if k[i] == k[len(k)-1-i]:
            b = True
            continue
        else:
            b = False
            break
    if b:
        print('Палиндромом.')
    else:
       print('Не палиндром.')
except:
    print('Ошибка ввода.')