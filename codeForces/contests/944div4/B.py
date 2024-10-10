
for _ in range(int(input())):
    a = input()
    ok = False
    for i in range(1, len(a)):
        if a[i] != a[0]:
            ok = True
            print("YES")
            print(a[i] + a[:i] + a[i+1:])
            break
    if not ok:
        print("NO")