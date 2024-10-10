def findCircleNum(adjacency):
    n = len(adjacency)
    visited = [False] * n
    comps = 0
    for i in range(n):
        if not visited[i]:
            comps += 1
            queue = [i]
            visited[i] = True
            while len(queue) > 0:
                k = queue.pop(0)
                for j in range(n):
                    if adjacency[k][j] == 1 and not visited[j]:
                        queue.append(j)
                        visited[j] = True
    return comps
        


adjacency = [[1,1,0],[1,1,0],[0,0,1]]
print(findCircleNum(adjacency))
adjacency = [[1,0,0],[0,1,0],[0,0,1]]
print(findCircleNum(adjacency))
adjacency = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
print(findCircleNum(adjacency))