
for _ in range(int(input())):
    s = input()
    if len(s) == 1:
        if s[0] == 'a':
            print(s + 'b')
        else:
            print(s + 'a')
    else:
        fet = False
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                if s[i] == 'a':
                    print(s[:i+1] + 'b' + s[i+1:])
                else:
                    print(s[:i+1] + 'a' + s[i+1:])
                fet = True
                break
        if not fet:
            if s[0] != 'a':
                print('a' + s)
            else:
                print('b' + s)