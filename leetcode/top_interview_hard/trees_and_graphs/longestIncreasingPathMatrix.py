def longestIncreasingPath(matrix):

    if len(matrix) == 0 or len(matrix[0]) == 0:
        return 0
    rows = len(matrix)
    cols = len(matrix[0])
    longest = [[-1 for i in range(cols)] for j in range(rows)]

    def findLongest(i,j):
        maxim = 0
        if i > 0 and matrix[i-1][j] < matrix[i][j]:
            if longest[i-1][j] == -1:
                findLongest(i-1,j)
            if longest[i-1][j] > maxim:
                maxim = longest[i-1][j]
        if i < rows-1 and matrix[i+1][j] < matrix[i][j]:
            if longest[i+1][j] == -1:
                findLongest(i+1,j)
            if longest[i+1][j] > maxim:
                maxim = longest[i+1][j]
        if j > 0 and matrix[i][j-1] < matrix[i][j]:
            if longest[i][j-1] == -1:
                findLongest(i,j-1)
            if longest[i][j-1] > maxim:
                maxim = longest[i][j-1]
        if j < cols-1 and matrix[i][j+1] < matrix[i][j]:
            if longest[i][j+1] == -1:
                findLongest(i,j+1)
            if longest[i][j+1] > maxim:
                maxim = longest[i][j+1]
        longest[i][j] = maxim + 1
        return
    
    maxPath = 1
    for i in range(rows):
        for j in range(cols):
            if longest[i][j] == -1:
                findLongest(i, j)
            if longest[i][j] > maxPath:
                maxPath = longest[i][j]

    print(longest)
    return maxPath


matrix = [[9,9,4],[6,6,8],[2,1,1]]
print(longestIncreasingPath(matrix))

matrix = [[3,4,5],[3,2,6],[2,2,1]]
print(longestIncreasingPath(matrix))