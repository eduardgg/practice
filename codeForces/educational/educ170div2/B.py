
t = int(input())
n = list(map(int, input().split()))
k = list(map(int, input().split()))
for e in k:
    print(pow(2, e, 10**9 + 7))