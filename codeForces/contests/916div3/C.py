
line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n, k = line()
    a = line()
    b = line()
    exp = 0
    bestb = 0
    suma = 0
    top = 0
    for i in range(min(k, n)):
        suma += a[i]
        bestb = max(bestb, b[i])
        top = max(top, suma + bestb*(k-i-1))
    print(top)