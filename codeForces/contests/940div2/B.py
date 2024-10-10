
line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n, k = line()
    if n == 1:
        print(k)
    elif not k&(k+1):
        a = [k] + [0 for _ in range(n-1)]
        print(*a)
    else:
        a0 = (1 << (k.bit_length()-1)) - 1
        a1 = k-a0
        a = [a0, a1] + [0 for _ in range(n-2)]
        print(*a)