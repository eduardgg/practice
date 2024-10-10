t = int(input())
for _ in range(t):
    n = int(input())
    S = [""]*n
    ans = 0
    for i in range(n):
        S[i] = input()
    for i in range(n//2):
        for j in range(i, n-i-1):
            nums = [ord(S[i][j]), ord(S[j][n-1-i]), ord(S[n-1-i][n-1-j]), ord(S[n-1-j][i])]
            maxOrd = max(nums)
            for num in nums:
                ans += maxOrd - num
    print(ans)