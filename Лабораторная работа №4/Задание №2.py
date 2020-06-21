from random import randint
x = int(input('Введите размер *массива*:'))
l = [randint(0,100) for i in range(x)]
s1 = []
s2 = []
for j in l:
    if j<50:
        s1.append(j)
    elif j>=50:
        s2.append(j)
print(l)
print(sum(s1)/len(s1))
print(sum(s2)/len(s2))