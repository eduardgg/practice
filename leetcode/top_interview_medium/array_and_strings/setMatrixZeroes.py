
def setMatrixZeroes(matrix):
    m = len(matrix)
    n = len(matrix[0])
    rows = [False]*m
    cols = [False]*n
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows[i] = True
                cols[j] = True
    for i in range(m):
        if rows[i] == True:
            for j in range(n):
                matrix[i][j] = 0
    for j in range(n):
        if cols[j] == True:
            for i in range(m):
                matrix[i][j] = 0
    return matrix


matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(setMatrixZeroes(matrix))
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(setMatrixZeroes(matrix))