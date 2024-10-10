for _ in range(int(input())):
    k = int(input())
    sizes = []
    for _ in range(k):
        n = int(input())
        sizes.append(n)
        p = list(map(int, input().split()))
    sizes.sort()
    ans = 0
    while sizes:
        s = sizes.pop()
        if (1 << (s.bit_length()-1)) & ans != 0:
            ans |= (1 << s.bit_length()-1) - 1
            break
        ans |= s
    print(ans)