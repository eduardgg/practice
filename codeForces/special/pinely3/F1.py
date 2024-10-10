t = int(input())
for _ in range(t):
    n = int(input())
    v = list(map(int, input().split()))
    comb = 1
    if v[-1] != n:
        print(0)
        continue
    for i in range(1, len(v)):
        if v[i-1] > i:
            comb = 0
            break
        dif = v[i]-v[i-1]
        if dif == 0:
            continue
        elif dif == 1:
            comb *= (2*(i-v[i-1])+1)
        elif dif == 2:
            comb *= (i-v[i-1])**2
        else:
            comb = 0
            break
        comb %= 998244353
    print(comb)