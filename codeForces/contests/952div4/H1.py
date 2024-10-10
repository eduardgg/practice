
for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    mat = []
    for i in range(n):
        mat.append(input())
    current = 0
    comps = [[-1 for _ in range(m)] for _ in range(n)]
    sizes = []
    for i in range(n):
        for j in range(m):
            if comps[i][j] == -1 and mat[i][j] == '#':
                stack = [(i, j)]
                comps[i][j] = current
                sizes.append(0)
                while stack:
                    sizes[-1] += 1
                    u, v = stack.pop()
                    if u+1 < n and mat[u+1][v] == '#' and comps[u+1][v] == -1:
                        stack.append((u+1, v))
                        comps[u+1][v] = current
                    if u-1 >= 0 and mat[u-1][v] == '#' and comps[u-1][v] == -1:
                        stack.append((u-1, v))
                        comps[u-1][v] = current
                    if v+1 < m and mat[u][v+1] == '#' and comps[u][v+1] == -1:
                        stack.append((u, v+1))
                        comps[u][v+1] = current
                    if v-1 >= 0 and mat[u][v-1] == '#' and comps[u][v-1] == -1:
                        stack.append((u, v-1))
                        comps[u][v-1] = current
                current += 1
    
    top = 0
    
    for i in range(n):
        setc = set()
        punts = 0
        for j in range(m):
            if mat[i][j] == '.':
                punts += 1
                if i-1 >= 0 and mat[i-1][j] == '#':
                    setc.add(comps[i-1][j])
                if i+1 < n and mat[i+1][j] == '#':
                    setc.add(comps[i+1][j])
            else:
                setc.add(comps[i][j])
        for co in setc:
            punts += sizes[co]
        top = max(top, punts)
        
    for j in range(m):
        setc = set()
        punts = 0
        for i in range(n):
            if mat[i][j] == '.':
                punts += 1
                if j-1 >= 0 and mat[i][j-1] == '#':
                    setc.add(comps[i][j-1])
                if j+1 < m and mat[i][j+1] == '#':
                    setc.add(comps[i][j+1])
            else:
                setc.add(comps[i][j])
        for co in setc:
            punts += sizes[co]
        top = max(top, punts)

    print(top)