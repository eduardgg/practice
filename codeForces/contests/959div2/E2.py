
for i in range(int(input())):
    k = int(input())
    ans = 0
    for _ in range(k):
        n = int(input())
        l = list(map(int, input().split()))
        if (1 << (n.bit_length()-1)) & ans != 0:
            ans |= ((1 << (n.bit_length()-1)) - 1)
        else:
            ans |= n
    print(ans)