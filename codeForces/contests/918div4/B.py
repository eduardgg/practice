
t = int(input())
for _ in range(t):
    for _ in range(3):
        s = input()
        if s[0] == '?' or s[1] == '?' or s[2] == '?':
            A = False
            B = False
            C = False
            for i in range(3):
                if s[i] == 'A':
                    A = True
                elif s[i] == 'B':
                    B = True
                elif s[i] == 'C':
                    C = True
            if not A:
                print("A")
            elif not B:
                print("B")
            else:
                print("C")