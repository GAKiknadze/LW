x,y = map(int,input('Введите диапазон значений(от X и Y): ').split())
for i in range(x,y+1):
    if i%2 == 1 and str(i) == str(i**2)[-len(str(i)):]:
        print(i)