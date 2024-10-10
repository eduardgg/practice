
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    j = -1
    ok = True
    for i in range(n):
        if not a[i] % a[0]:
            continue
        elif j == -1:
            j = i
        elif a[i] % a[j]:
            ok = False
            break
    print("Yes" if ok else "No")