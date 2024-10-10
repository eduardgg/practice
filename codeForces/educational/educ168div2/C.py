
for _ in range(int(input())):
    n = int(input())
    s = input()
    pos = [0]
    cost = 0
    for i in range(1, n, 2):
        if s[i] == '(':
            pos.append(i)
        else:
            cost += (i - pos.pop())
        if pos:
            cost += (i + 1 - pos.pop())
        else:
            pos.append(i + 1)
    print(cost)