def lastLessThan(vector, target):
    # Retorna l'índex de l'últim element del vector
    # estrictament menor al target.
    low = 0
    high = len(vector) - 1
    if vector[low] >= target:
        return low-1
    if vector[high] < target:
        return high
    if len(vector) == 2:
        return low
    med = (low + high) // 2
    if vector[med] >= target:
        return lastLessThan(vector[:med], target)
    return med + lastLessThan(vector[med:], target)


def searchMatrix(matrix, target):

    print(matrix)
    
    if matrix == [] or matrix[0] == []:
        return False

    # Podem columnes per la dreta:
    i = lastLessThan(matrix[0], target)
    if i < len(matrix[0])-1:
        if matrix[0][i+1] == target:
            return True
    if i == -1:
        return False
    
    # Podem columnes per l'esquerra:
    p = lastLessThan(matrix[-1], target)
    if p == len(matrix[0])-1:
        return False
    if p < len(matrix[0])-1:
        if matrix[-1][p+1] == target:
            return True

    # Podem files per sota:
    j = lastLessThan([matrix[k][0] for k in range(len(matrix))], target)
    if j < len(matrix)-1:
        if matrix[j+1][0] == target:
            return True
    
    # Podem files per sobre:
    q = lastLessThan([matrix[k][-1] for k in range(len(matrix))], target)
    if q < len(matrix)-1:
        if matrix[q+1][-1] == target:
            return True
    
    newMatrix = [[matrix[m][n] for n in range(p+1,i+1)] for m in range(q+1,j+1)]
    return searchMatrix(newMatrix, target)


matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
print(searchMatrix(matrix, 5))
print(searchMatrix(matrix, 10))
print(searchMatrix(matrix, 12))
print(searchMatrix([[-1,3]], 1))
print(searchMatrix([[1],[3],[5]], 2))
print(searchMatrix([[1,4],[2,5]], 3))


"""
print(lastLessThan(matrix[0],10))
print(lastLessThan(matrix[2],20))
print(lastLessThan(matrix[4],9))
print(lastLessThan(matrix[4],31))
print(lastLessThan(matrix[0],11))
"""