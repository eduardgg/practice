
m = int(input())
q = [0 for _ in range(50)]
for _ in range(m):
    t, x = list(map(int, input().split()))
    if t == 1:
        q[x] += 1
        while q[x] > 2:
            c = (q[x]-1)//2
            q[x+1] += c
            q[x] -= 2*c
            x += 1
    else:
        ok = True
        i = 0
        rem = 0
        while x > 0 and i < len(q):
            rem += q[i]
            if x % 2 and rem == 0:
                ok = False
                break
            x //= 2
            rem //= 2
            i += 1
        if not ok:
            print("NO")
        else:
            print("YES")