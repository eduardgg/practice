
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
    res = [[(i == j) for i in range(6)] for j in range(6)]
    while n:
        if n & 1:
            res = mult(res, mat, mod)
        mat = mult(mat, mat, mod)
        n >>= 1
    return res


mat = [
    [1,1,1,1,1,1],
    [1,0,0,0,0,0],
    [0,1,0,0,0,0],
    [0,0,1,0,0,0],
    [0,0,0,1,0,0],
    [0,0,0,0,1,0]
    ]

MOD = 10**9 + 7
n = int(input())
if n < 6:
    print(1 << (n-1))
else:
    mat = pow(mat, n-6, MOD)
    init = [[1 << i] for i in range(5, -1, -1)]
    res = mult([mat[0]], init, MOD)[0][0]
    print(res)