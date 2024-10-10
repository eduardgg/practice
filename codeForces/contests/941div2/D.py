
for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    v = []
    i = 0
    suma = 0
    while suma + (1<<i) < k:
        v.append(1<<i)
        suma += (1<<i)
        i += 1
    if k - (1<<i):
        v.append(k - (1<<i))
    if n >= k+1 and (k+1)&k:
        v.append(k+1)
    i += 1
    if n >= (1<<i) + k:
        v.append((1<<i) + k)
    while len(v) < 25 and 1<<i <= n:
        v.append(1<<i)
        i += 1
    print(len(v))
    print(*v)