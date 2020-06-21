p = 2
while True:
    if all(p % i for i in range(2, p)):
        k = 2**(p-1)*(2**p-1)
        if k%3 == 0 and k%5 == 0:
            print(k)
    if k > 10 ** 10:
        break
    p+=1