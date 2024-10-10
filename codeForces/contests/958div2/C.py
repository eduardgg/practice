
for _ in range(int(input())):
    n = int(input())
    ans = [n]
    for i in range(n.bit_length()):
        if n & (1 << i) and (n - (1 << i)):
            ans.append(n - (1 << i))
    ans = ans[::-1]
    print(len(ans))
    print(*ans)