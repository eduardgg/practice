
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    even = True
    quad = False
    for e in a:
        if e == 0:
            even = True
            quad = False
        elif e <= 2:
            if not quad:
                ans += 1
                quad = True
            elif not even:
                ans += 1
                even = True
            else:
                quad = False
            even = True
        elif e <= 4:
            ans += 1
            even = not even
        else:
            ans += 1
            quad = False
            even = True
    
    print(ans)