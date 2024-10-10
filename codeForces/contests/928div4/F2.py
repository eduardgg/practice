
line = lambda : list(map(int, input().split()))

def f1(m, k):
    if k >= best1[0]:
        return
    for i in range(5):
        for j in range(5):
            if (i+j) % 2 == 0:
                continue
            if m[i][j] == 'B' and m[i][j+2] == 'B' and m[i+2][j] == 'B' and m[i+2][j+2] == 'B' and m[i+1][j+1] == 'B':
                
                m[i][j] = 'W'
                f1(m, k+1)
                m[i][j] = 'B'

                m[i][j+2] = 'W'
                f1(m, k+1)
                m[i][j+2] = 'B'

                m[i+2][j] = 'W'
                f1(m, k+1)
                m[i+2][j] = 'B'

                m[i+1][j+1] = 'W'
                f1(m, k+1)
                m[i+1][j+1] = 'B'

                m[i+2][j+2] = 'W'
                f1(m, k+1)
                m[i+2][j+2] = 'B'

                return
    
    best1[0] = min(best1[0], k)
    return

def f2(m, k):
    if k >= best2[0]:
        return
    for i in range(5):
        for j in range(5):
            if (i+j) % 2 != 0:
                continue
            if m[i][j] == 'B' and m[i][j+2] == 'B' and m[i+2][j] == 'B' and m[i+2][j+2] == 'B' and m[i+1][j+1] == 'B':
                
                m[i][j] = 'W'
                f2(m, k+1)
                m[i][j] = 'B'

                m[i][j+2] = 'W'
                f2(m, k+1)
                m[i][j+2] = 'B'

                m[i+2][j] = 'W'
                f2(m, k+1)
                m[i+2][j] = 'B'

                m[i+1][j+1] = 'W'
                f2(m, k+1)
                m[i+1][j+1] = 'B'

                m[i+2][j+2] = 'W'
                f2(m, k+1)
                m[i+2][j+2] = 'B'

                return
    
    best2[0] = min(best2[0], k)
    return
    

for _ in range(int(input())):
    best1 = [49]
    best2 = [49]
    mat = []
    for i in range(7):
        s = input()
        mat.append([e for e in s])
    f1(mat, 0)
    f2(mat, 0)
    ans = best1[0] + best2[0]
    print(ans)