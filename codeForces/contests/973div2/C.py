
for _ in range(int(input())):
    
    n = int(input())
    ans = []
    
    while len(ans) < n:
        print('? ' + ''.join(ans) + '1', flush=True)
        if input() == '1':
            ans.append('1')
        else:
            print('? ' + ''.join(ans) + '0', flush=True)
            if input() == '1':
                ans.append('0')
            else:
                break
    
    ans = ans[::-1]

    while len(ans) < n:
        print('? ' + '1' + ''.join(ans[::-1]), flush=True)
        ans.append(input())
    
    ans = ans[::-1]
    print('! ' + ''.join(ans), flush=True)