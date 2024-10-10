
def mcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mcm(a, b):
    if a == 0 or b == 0:
        return 0
    else:
        return abs(a * b) // mcd(a, b)
    
t = int(input())
for _ in range(t):
    a, b = list(map(int, input().split()))
    m = mcm(a,b)
    if b%a == 0:
        print(m*b//a)
    else:
        print(m)