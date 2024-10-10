
for _ in range(int(input())):
    x, y = list(map(int, input().split()))
    exp = 0
    xor = x^y
    while xor % 2 == 0:
        exp += 1
        xor //= 2
    print(2**exp)