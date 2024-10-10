
line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    a = line()
    s = set(a)
    for i in range(n+1):
        if i not in s:
            mex = i
            break
    if mex == 0:
        print(2)
        print(1, 1)
        print(2, n)
        continue
    found = set()
    i = 0
    while i < n and len(found) < mex:
        if a[i] < mex and a[i] not in found:
            found.add(a[i])
        i += 1
    found = set()
    j = i
    while j < n and len(found) < mex:
        if a[j] < mex and a[j] not in found:
            found.add(a[j])
        j += 1
    if len(found) < mex:
        print(-1)
    else:
        print(2)
        print(1, i)
        print(i+1, n)