
# En aquesta extensió del problema P11455, retornem l'ordre òptim dels productes matricials.
# Si l'entrada és m, hi ha m-1 matrius. Les anomenem totes igual (A), però cal entendre que
# les seves dimensions estan en el mateix ordre que el donat, per parells consecutius.

def f(i, j):
    if F[i][j] != -1:
        return (F[i][j], M[i][j])
    if (j == i+1):
        return (0, -1)
    minim = float('inf')
    for k in range(i+1, j):
        e = f(i, k)[0] + f(k, j)[0] + dims[i]*dims[k]*dims[j]
        if e < minim:
            posMin = k
            minim = e
    F[i][j] = minim
    M[i][j] = posMin
    return (minim, posMin)

def optimalProduct(i, j):
    if (j == i+1):
        return "A"
    if (j == i+2):
        return "(A·A)"
    return "(" + optimalProduct(i, M[i][j]) + "·" + optimalProduct(M[i][j], j) + ")"

while True:
    dims = list(map(int, input().split()))
    m = int(dims.pop(0))
    F = [[-1] * (m+1) for _ in range(m+1)]
    M = [[-1] * (m+1) for _ in range(m+1)]
    optim = f(0, m)[0]
    print("Cost del producte òptim: ", optim)
    print(optimalProduct(0, m))