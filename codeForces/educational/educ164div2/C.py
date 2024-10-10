
for _ in range(int(input())):
    
    x = input()
    y = input()
    n = len(x)
    i = 0
    while i < n and x[i] == y[i]:
        i += 1
    if i == n:
        print(x)
        print(y)
        continue
    ansx = [e for e in x[:i]] + [str(max(int(x[i]), int(y[i])))]
    ansy = [e for e in x[:i]] + [str(min(int(x[i]), int(y[i])))]
    i += 1
    while i < n:
        ansx.append(str(min(int(x[i]), int(y[i]))))
        ansy.append(str(max(int(x[i]), int(y[i]))))
        i += 1
    print(''.join(ansx))
    print(''.join(ansy))
