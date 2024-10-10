
for _ in range(int(input())):
    n = int(input())
    if n%10 == 9:
        print("NO")
        continue
    n //= 10
    ok = True
    while n >= 10:
        if not n%10:
            ok = False
            break
        n //= 10
    if n != 1:
        ok = False
    print("YES" if ok else "NO")