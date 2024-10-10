
def troba(x, v):
    esquerra = 0
    dreta = len(v) - 1
    while esquerra <= dreta:
        mig = (esquerra + dreta) // 2
        if v[mig] <= x < v[mig + 1]:
            return mig
        elif v[mig] < x:
            esquerra = mig + 1
        else:
            dreta = mig - 1
    return None


t = int(input())
for _ in range(t):
    
    n, k = list(map(int, input().split()))
    s = input()
    l = list(map(int, input().split()))
    r = list(map(int, input().split()))
    q = int(input())
    xs = list(map(int, input().split()))
    
    if n == 1:
        print(s)
        continue
    
    # Permutació per més eficiència (?)
    p = [i for i in range(n)]
    for x in xs:
        i = troba(x, l + [r[-1]])
        a = min(x, r[i] + l[i] - x) - 1
        b = max(x, r[i] + l[i] - x) - 1
        for j in range(a, (a+b)//2 + 1):
            p[j], p[b+a-j] = p[b+a-j], p[j] 
    for e in p:
        print(s[e], end="")
    print()