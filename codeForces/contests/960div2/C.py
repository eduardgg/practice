
for _ in range(int(input())):
    
    n = int(input())
    a = list(map(int, input().split()))
    
    ans = sum(a)

    s = set()
    b = []
    maxim = 0
    for e in a:
        if e in s and e > maxim:
            maxim = e
        s.add(e)
        b.append(maxim)
    
    ans += sum(b)
    
    s = set()
    c = []
    maxim = 0
    for e in b:
        if e in s and e > maxim:
            maxim = e
        s.add(e)
        c.append(maxim)
    
    for i in range(n):
        ans += c[i]*(n-i)
    
    print(ans)