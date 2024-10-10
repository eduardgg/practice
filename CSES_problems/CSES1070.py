
n = int(input())
if n in {2, 3}:
    print("NO SOLUTION")
elif n == 4:
    print("3 1 4 2")
else:
    ans = []
    for i in range(n//2):
        ans.append(n-i)
        ans.append(n//2-i)
    if n%2: ans.append(n-n//2)
    print(*ans)