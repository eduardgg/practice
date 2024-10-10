

# Programació dinàmica en la que els elements input són "trams" de vector, que
# també es pot expressar com un parell d'índexos (emmagatzemats en una matriu).
# Retornar el mínim producte per cada separació possible escollida.

def f(i, j):
    if F[i][j] != -1:
        return F[i][j]
    if (j-i == 1):
        return 0
    minim = float('inf')
    for k in range(i+1, j):
        e = f(i, k) + f(k, j) + dims[i]*dims[k]*dims[j]
        if e < minim:
            posMin = k
            minim = e
    print(posMin)
    F[i][j] = minim
    return F[i][j]

while True:
    dims = list(map(int, input().split()))
    m = int(dims.pop(0))
    F = [[-1] * (m+1) for _ in range(m+1)]
    optim = f(0, m)
    print(optim)