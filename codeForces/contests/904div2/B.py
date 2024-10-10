
for _ in range(int(input())):
    n = int(input())
    a = input()

    swaps = 0
    ans = [0]
    for i in range(n):
        if a[-1-i] == '1':
            swaps += 1
        else:
            ans.append(ans[-1]+swaps)

    ans.pop(0)
    for i in range(n-len(ans)):
        ans.append(-1)
    
    print(*ans)