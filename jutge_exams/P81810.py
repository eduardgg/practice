
def f(i, j, o):
    
    if (i == 0) and (j == 0):
        if (o == 0 and linies[0][0] == '.') or (o == 1 and linies[0][0] == 'X'):
            return 1
        return 0
    
    if (o < 0) or (i < 0) or (j < 0):
        return 0
    
    if F[i][j][o] != -1:
        return F[i][j][o]

    if linies[i][j] == 'X':
        F[i][j][o] = f(i-1, j, o-1) + f(i, j-1, o-1)
        return F[i][j][o]

    F[i][j][o] = f(i-1, j, o) + f(i, j-1, o)
    return F[i][j][o]
    


while True:
    linia = input().split(" ")
    n, m, k = (int(linia[0]), int(linia[1]), int(linia[2]))
    linies = []
    for i in range(n):
        linies += [input()]
        F = [[[-1 for _ in range(k+1)] for _ in range(m)] for _ in range(n)]
    print(f(n-1, m-1, k))    
    linia = input()