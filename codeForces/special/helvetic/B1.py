
n = int(input())
a = list(map(int, input().split()))
v = [(a[i], i) for i in range(n)]
v.sort()

for i in range(1, n):
    print(n-i, )