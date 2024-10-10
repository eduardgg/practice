t = int(input())
for _ in range(t):
    s = input()
    trobat = False
    for i in range(1, len(s)):
        if s[i] != '0' and int(s[:i]) < int(s[i:]):
            print(s[:i], " ", s[i:])
            trobat = True
            break
    if not trobat:
        print(-1)