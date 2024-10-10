def maximalRectangle(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    Mx = []
    My = []
    for i in range(rows):
        Mx.append([0]*cols)
        My.append([0]*cols)
    return Mx, My




matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(maximalRectangle(matrix))

"""
Vigilar molt amb això: (No fer-ho)
matrix = [[[0]*3]*3]*3
matrix [0][0][0] = 1
"""