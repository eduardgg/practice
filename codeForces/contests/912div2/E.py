
line = lambda : list(map(int,input().split()))

for _ in range(int(input())):
    n = int(input())
    sx, sy = line()
    suma = 0
    odd, even = set(), set()
    for i in range(n):
        x, y = line()
        z = ((x-sx) & 1) ^ ((y-sy) & 1)
        suma ^= z
        if z:
            odd.add(i+1)
        else:
            even.add(i+1)
    
    if len(even) >= len(odd):
        print("First", flush=True)
        for i in range(n):
            if i&1:
                e = int(input())
                if e in odd:
                    odd.remove(e)
                else:
                    even.remove(e)
            elif odd:
                print(odd.pop(), flush=True)
            else:
                print(even.pop(), flush=True)

    else:
        print("Second", flush=True)
        for i in range(n):
            if not i&1:
                e = int(input())
                if e in odd:
                    odd.remove(e)
                else:
                    even.remove(e)
            elif even:
                print(even.pop(), flush=True)
            else:
                print(odd.pop(), flush=True)