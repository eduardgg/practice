
line = lambda : list(map(int, input().split()))
for _ in range(int(input())):
    n, c = line()
    s = line()
    e, o = 0, 0
    A, B = 0, 0
    for i in s:
        e += (i+1)%2
        o += i%2
        A += (i+2)//2
        B += (c-i+1)
    
    C = e*(e+1)//2 + o*(o+1)//2
    E = (c+1)*(c+2)//2
    ans = E - A - B + C
    print(ans)