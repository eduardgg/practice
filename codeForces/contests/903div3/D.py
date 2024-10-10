
# Està bé però el Jutge diu que Wrong Answer...
# (per algun cas, l'expected és "NO", i l'output és "YES")

# ERATHOSTENES:
v = [0, 0] + [1]*(1000-1)
for i in range(2, 1000+1):
    if v[i] == 0:
        continue
    if v[i] == 1:
        j = 2*i
        while j <= 1000:
            v[j] = 0
            j += i
primers = [p for p in range(1000+1) if v[p] == 1] 

t = int(input())
for _ in range(t):
    n = int(input())
    v = list(map(int, input().split()))
    
    for p in primers:
        mult = 0
        for i in range(n):
            while v[i] % p == 0:
                v[i] //= p
                mult += 1
        if mult % n != 0:
            print("NO")
            break
        if max(v) == min(v):
            print("YES")
            break