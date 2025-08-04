
def mult(mat1, mat2, mod):
    if len(mat1[0]) != len(mat2):
        print("Error: multiplicació matricial invàlida")
        return
    m, n, l = len(mat1), len(mat1[0]), len(mat2[0])
    mat = [[0 for _ in range(l)] for _ in range(m)]
    for i in range(m):
        for j in range(l):
            for k in range(n):
                mat[i][j] = (mat[i][j] + mat1[i][k]*mat2[k][j]) % mod
    return mat

def pow(mat, n, mod):
    if len(mat) != len(mat[0]):
        print("Error: Matriu no quadrada")
        return
    res = [[int(i == j) for i in range(len(mat))] for j in range(len(mat))]
    while n:
        if n & 1:
            res = mult(res, mat, mod)
        mat = mult(mat, mat, mod)
        n >>= 1
    return res


mat = [ [1,1], [1,0] ]

MOD = 10**9 + 7
n = int(input())
if n < 2:
    print(n)
else:
    mat = pow(mat, n-1, MOD)
    init = [[1], [0]]
    res = mult([mat[0]], init, MOD)[0][0]
    print(res)