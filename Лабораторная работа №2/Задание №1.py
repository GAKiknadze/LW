try:
    a, b = map(int, input("Введите два целых числа: ").split())
    print("a =", a, "b = ", b)
    print("Замена с помощью третьей переменной:")
    c = a
    a = b
    b = c
    print("a =", a, "b = ", b)
    print("Замена с помощью кортежа")
    cort = (a, b)
    a, b = b, a
    print("a =", a, "b = ", b)
    print("Замена без использования других переменных")
    a += b
    b = a - b
    a -= b
    print("a =", a, "b = ", b)
except ValueError:
    print('Ошибка ввода.')