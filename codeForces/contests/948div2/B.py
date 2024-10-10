
for _ in range(int(input())):
    n = int(input())
    a = []

    while n:
        if not n%2:
            a.append(0)
            n //= 2
        elif n%4 == 1:
            a.append(1)
            n //= 2
            if n:
                a.append(0)
                n //= 2
        else:
            a.append(-1)
            n = (n+1)//2
            if n:
                a.append(0)
                n //= 2

    print(len(a))
    print(*a)