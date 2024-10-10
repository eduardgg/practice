
n, q = list(map(int, input().split()))
a = list(map(int, input().split()))
for _ in range(q):
    l, r = list(map(int, input().split()))
    if r-l >= 50:
        print("YES")
    else:
        v = a[l-1:r]
        v.sort()
        ok = False

        for i in range(r-l-4):
            if v[i] + v[i+1] > v[i+2] and v[i+3] + v[i+4] > v[i+5]: ok = True; break
            if v[i] + v[i+1] > v[i+3] and v[i+2] + v[i+4] > v[i+5]: ok = True; break
            if v[i] + v[i+1] > v[i+4] and v[i+2] + v[i+3] > v[i+5]: ok = True; break
            if v[i] + v[i+1] > v[i+5] and v[i+2] + v[i+3] > v[i+4]: ok = True; break
            if v[i] + v[i+2] > v[i+3] and v[i+1] + v[i+4] > v[i+5]: ok = True; break
            if v[i] + v[i+2] > v[i+4] and v[i+1] + v[i+3] > v[i+5]: ok = True; break
            if v[i] + v[i+2] > v[i+5] and v[i+1] + v[i+3] > v[i+4]: ok = True; break
            if v[i] + v[i+3] > v[i+4] and v[i+1] + v[i+2] > v[i+5]: ok = True; break
            if v[i] + v[i+3] > v[i+5] and v[i+1] + v[i+2] > v[i+4]: ok = True; break
            if v[i] + v[i+4] > v[i+5] and v[i+1] + v[i+2] > v[i+3]: ok = True; break
        
        if ok: print("YES"); continue

        t1 = False
        for i in range(r-l-4):
            if v[i] + v[i+1] > v[i+2]:
                t1 = True
                ind = i+3
                break

        if not t1: print("NO"); continue

        t2 = False
        for i in range(ind, r-l-1):
            if v[i] + v[i+1] > v[i+2]:
                t2 = True
                break
        
        print("YES" if t2 else "NO")