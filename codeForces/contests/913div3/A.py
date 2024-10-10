
line = lambda : list(map(int, input().split()))
num = "12345678"
abc = "abcdefgh"
for _ in range(int(input())):
    s = input()
    for i in num:
        if s[1] != i:
            print(s[0] + i)
    for i in abc:
        if s[0] != i:
            print(i + s[1])