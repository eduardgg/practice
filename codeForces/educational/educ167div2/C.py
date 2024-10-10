
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    pa, pb = 0, 0
    neg, pos = 0, 0
    for i in range(n):
        if a[i] > b[i]:
            pa += a[i]
        elif b[i] > a[i]:
            pb += b[i]
        elif a[i] + b[i] == 2:
            pos += 1
        elif a[i] + b[i] == -2:
            neg += 1
    if pa < pb:
        pa, pb = pb, pa
    if pa - neg >= pb + pos:
        ans = pb + pos
    else:
        pos -= (pa - pb)
        ans = pa - (neg-pos+1)//2
    print(ans)