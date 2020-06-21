import math
x,y = map(int,input('Введите диапазон значений(от X и Y): ').split())

def is_prime(a):
    if a < 2:
        return False
    return all(a % i for i in range(2, a))

for i in range(x,y):
    if is_prime(i):
        print(i, end=' | ')