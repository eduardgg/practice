
def f(suma, n, i):
    if D.get((suma, i), False):
        return D[(suma, i)]
    if suma < 0:
        return False
    if (i == n) or suma < 0:
        return False
    F1 = f(suma, n, i+1)
    F2 = f(suma - nombres[i], n, i+1)
    D[(suma, i)] = F1 or F2
    return D[(suma, i)]

while True:
    nombres = list(map(int, input().split()))
    suma = nombres.pop(0)
    n = nombres.pop(0)
    D = dict()
    D[(0, n)] = True
    F = f(suma, n, 0)
    sumands = []
    print(suma, end = " = ")
    for i in range(n):
        if D.get((suma - nombres[i], i+1), False):
            sumands += [nombres[i]]            
            suma -= nombres[i]
    ultim = sumands.pop()
    for s in sumands:
        print(s, end = " + ")
    print(ultim)