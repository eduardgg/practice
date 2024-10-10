
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    i = 0
    while i < n and a[i] <= a[k-1]:
        i += 1
    if i >= k:
        print(i-1)
        continue
    j = i+1
    while j < n and a[j] < a[k-1]:
        j += 1
    print(max(i-1, j-i-1 + (i!=0)))