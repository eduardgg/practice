def isHappy(n):
    n = sum([int(str(n)[i])**2 for i in range(len(str(n)))])
    vist = [0]*1000
    while (vist[n] == 0) and n != 1:
        vist[n] = 1
        n = sum([int(str(n)[i])**2 for i in range(len(str(n)))])
    if n == 1:
        return True
    return False

n = 19
print(isHappy(n))

n = 2
print(isHappy(n))