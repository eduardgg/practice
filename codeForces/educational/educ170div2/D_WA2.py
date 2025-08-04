
n, m = list(map(int, input().split()))
r = list(map(int, input().split()))

i = 0
prefix = [0 for _ in range(m+2)]

for e in r:
    if e == 0:
        i += 1
    elif 0 < e < i+1: 
        prefix[e] += 1
        prefix[i+1] -= 1
    elif 0 < -e < i+1:
        prefix[0] += 1
        prefix[i-(-e)+1] -= 1

maxim = 0
suma = 0
for e in prefix:
    suma += e
    maxim = max(maxim, suma)

print(maxim)