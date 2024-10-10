
t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(n//2):
        print((10**(n//2)+(3*10**i))**2)
    for i in range(n//2):
        print((3*10**(n//2)+(10**i))**2)
    print((10**(n//2) + 4*10**(n//2)//10)**2)