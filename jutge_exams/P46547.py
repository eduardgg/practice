
def f(m, n, j, u, res, punts):
    if (u == n):
        return punts
    maxim = 0
    for i in range(n):
        residu = (res+i+1) % m
        if not usat[i] and residu != 0:
            usat[i] = True
            if (u == 0):
                F = f(m, n, i, u+1, residu, punts)                
            else:
                F = f(m, n, i, u+1, residu, punts + matriu[j][i])                
            if F > maxim:
                maxim = F
            usat[i] = False
    if maxim > 0:
        return maxim
    return -10**9


while True:
    linia = input().split(" ")
    m, n = (int(linia[0]), int(linia[1]))
    matriu = []
    for _ in range(n):
        fila = list(map(int, input().split()))
        matriu.append(fila)
    usat = [False]*n
    resultat = f(m, n, -1, 0, 0, 0)

    if resultat < 0:
        print("0")
    else:
        print(resultat)
    _ = input()