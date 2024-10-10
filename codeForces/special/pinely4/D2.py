
ans1 = [0, 1, 2, 2, 3, 3]
colors1 = [0, 1, 2, 2, 3, 1]
colors2 = [0, 1, 4, 2, 3, 1, 4]

for i in range(2*(10**5)):
    colors2.append(colors2[-4])

for _ in range(int(input())):
    n = int(input())
    if n <= 5:
        print(ans1[n])
        print(*colors1[1:n+1])
    else:
        print(4)
        print(*colors2[1:n+1])