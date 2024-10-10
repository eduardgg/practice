
def f(n, m, i, j):

    if (j == n):
        # print(matriu)
        return 1
    
    if (matriu[j][i] == 'X') or (matriu[j][i] == 'O'):
        if i < m-1:
            return f(n, m, i+1, j)
        else:
            return f(n, m, 0, j+1)
    
    X = 0
    if (rowsX[j] < m - rows[j]) and (colsX[i] < n - cols[i]):
        matriu[j][i] = 'X'
        rowsX[j] += 1
        colsX[i] += 1
        if i < m-1:
            X = f(n, m, i+1, j)
        else:
            X = f(n, m, 0, j+1)
        rowsX[j] -= 1
        colsX[i] -= 1
        matriu[j][i] = '.'

    O = 0
    if (rowsO[j] < rows[j]) and (colsO[i] < cols[i]):
        matriu[j][i] = 'O'
        rowsO[j] += 1
        colsO[i] += 1
        if i < m-1:
            O = f(n, m, i+1, j)
        else:
            O = f(n, m, 0, j+1)
        rowsO[j] -= 1
        colsO[i] -= 1
        matriu[j][i] = '.'
        
    return X + O



while True:
    linia = input().split(" ")
    n, m = (int(linia[0]), int(linia[1]))
    matriu = []
    rowsO = [0]*n
    colsO = [0]*m
    rowsX = [0]*n
    colsX = [0]*m
    for j in range(n):
        fila = list(input())
        matriu.append(fila)
        for i in range(m):
            if matriu[j][i] == 'O':
                rowsO[j] += 1
                colsO[i] += 1
            if matriu[j][i] == 'X':
                rowsX[j] += 1
                colsX[i] += 1
    rows = list(map(int, input().split()))
    cols = list(map(int, input().split()))
    resultat = f(n, m, 0, 0)
    print(resultat)
    _ = input()