
# CSES 1087 - Shortest Subsequence
# https://cses.fi/problemset/task/1087

def longestADN(s):
    vist = set()
    ans = []
    for c in s:
        vist.add(c)
        if len(vist) == 4:
            ans.append(c)
            vist = set()
    for c in 'ACGT':
        if c not in vist:
            ans.append(c)
            break
    return ''.join(ans)

s = 'ACGTACGT'
print(longestADN(s))