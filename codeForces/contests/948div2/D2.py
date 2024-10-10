
line = lambda : list(map(int, input().split()))

def f(i, cjt):
    global v
    if len(cjt) <= top[0]:
        return 0
    
    if i == n:
        ans = len({e for e in cjt if v[e] == 1})
        if ans > top[0]:
            top[0] = ans
            topstr[0] = ''.join(xor)
        return ans
    
    backup = [e for e in v]
    cjt1 = {e for e in cjt}
    xor[i] = '0'
    for j in cjt:
        v[j] += int(mat[i][j])
        if v[j] > 1: cjt1.remove(j)
    ans1 = f(i+1, cjt1)

    v = [e for e in backup]
    cjt2 = {e for e in cjt}
    xor[i] = '1'
    for j in cjt:
        v[j] += 1-int(mat[i][j])
        if v[j] > 1: cjt2.remove(j)
    ans2 = f(i+1, cjt2)

    return max(ans1, ans2)



for _ in range(int(input())):
    n, m = line()
    mat = []
    v = [0 for _ in range(m)]
    xor = ['-1' for _ in range(n)]
    for i in range(n):
        mat.append(input())
    cjt = {i for i in range(m)}
    top = [0]
    topstr = ['']
    ans = f(0, cjt)
    print(top[0])
    print(topstr[0])