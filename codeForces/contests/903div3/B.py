t = int(input())
for _ in range(t):
    v = list(map(int, input().split()))
    v.sort()
    if v[0] == v[1]:
        if v[2]/v[1] in {1,2,3,4}:
            print("YES")
        else:
            print("NO")
    elif 2*v[0] == v[1]:
        if v[2]/v[0] in {2,3}:
            print("YES")
        else:print("NO")
    else:
        print("NO")