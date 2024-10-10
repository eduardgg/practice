

def f(n, k):
    if n == 1:
        return 0
    elif k >= n:
        return 1
    return 1 + f(n-k+1, k)

for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    print(f(n, k))