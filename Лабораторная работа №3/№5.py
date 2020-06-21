from itertools import combinations_with_replacement
p = 0
l = []

for k in range(1,11):
    a = [i ** k for i in range(10)]
    for b in combinations_with_replacement(range(10), k):
        x = sum(map(lambda y: a[y], b))
        if x > 0 and tuple(int(d) for d in sorted(str(x))) == b:
            l.append(x)
print(l)
print(max(l))
