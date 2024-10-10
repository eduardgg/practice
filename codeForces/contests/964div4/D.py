
for _ in range(int(input())):
    
    s = input()
    t = input()
    post = 0
    word = []

    for i in range(len(s)):
        if s[i] in {'?', t[post]}:
            word.append(t[post])
            post += 1
        else:
            word.append(s[i])
        if post == len(t):
            poss = i+1
            break
    
    if post < len(t):
        print("NO")
    else:
        print("YES")
        for i in range(poss, len(s)):
            word.append(s[i] if s[i] != '?' else 'a')
        w = ''.join(word)
        print(w)