
for _ in range(int(input())):
    x, k = list(map(int, input().split()))
    i = 0
    while True:
        c = x+i
        suma = 0
        while c:
            suma += c%10
            c //= 10
        if not suma%k:
            print(x+i)
            break
        i += 1