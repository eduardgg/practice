		
n, m = map(int, input().split())
r = list(map(int, input().split()))
prefix = [0 for _ in range(m+2)]
z = 0

for e in r:
    if e == 0:
        for i in range(1, m+1): prefix[i] += prefix[i-1]
        for i in range(m, 0, -1): prefix[i] = max(prefix[i], prefix[i-1])
        for i in range(m, 0, -1): prefix[i] -= prefix[i-1]
        z += 1
    elif 0 < e <= z:
        prefix[e] += 1
        prefix[z+1] -= 1
    elif 0 < -e <= z:
        prefix[0] += 1
        prefix[z-(-e)+1] -= 1

for i in range(1, m+1): prefix[i] += prefix[i-1]
print(max(prefix))