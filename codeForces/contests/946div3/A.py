
for _ in range(int(input())):
    x, y = list(map(int, input().split()))
    scr = (y+1)//2
    sobra = 15*scr - 4*y
    x -= sobra
    if x > 0:
        scr += x//15 + (x%15 != 0)
    print(scr)