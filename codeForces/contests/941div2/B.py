
for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    mat = []
    for i in range(n):
        mat.append(input())
    bu, bd, bl, br = False, False, False, False
    wu, wd, wl, wr = False, False, False, False
    for i in mat[0]:
        if i == 'W':
            wu = True
        else:
            bu = True
    for i in mat[-1]:
        if i == 'W':
            wd = True
        else:
            bd = True
    for i in range(n):
        if mat[i][0] == 'W':
            wl = True
        else:
            bl = True
    for i in range(n):
        if mat[i][-1] == 'W':
            wr = True
        else:
            br = True
    if (bu and bd and bl and br) or (wu and wd and wl and wr):
        print("YES")
    else:
        print("NO")