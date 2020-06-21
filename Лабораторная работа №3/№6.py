x = int(input('Введите число: '))
z1 = (1+5**0.5)/2
z2 = (1-5**0.5)/2
k = 5**0.5
i = 0
g = 0
while True:
    f = int((z1**i-z2**i)/k)
    if g == 20:
        break
    if f>x:
        print(f)
        g+=1
    i+=1