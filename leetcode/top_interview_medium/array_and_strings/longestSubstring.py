def longestSubstring(s):
    dict = {}
    leng = 0
    maxlen = 0
    for i in range(len(s)):
        if s[i] not in dict.keys() or dict[s[i]] < i - leng:
            leng = leng + 1
        else:
            leng = i - dict[s[i]]
        dict[s[i]] = i
        maxlen = max(maxlen, leng)
    return maxlen

s = "abcabcbb"
print(longestSubstring(s))
s = "abcdeafbdgcbb"
print(longestSubstring(s))