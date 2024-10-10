def strToMultiset(s):
    mset = {}
    for i in s:
        mset[i] = mset.get(i,0) + 1
    return mset

def groupAnagrams(strs):
    msets = []
    output = []
    for s in strs:
        charset = strToMultiset(s)
        if charset not in msets:
            msets.append(charset)
            output += [[s]]
            continue
        ind = msets.index(charset)
        output[ind] += [s]
    return output

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))
strs = ["eat","tan"]
print(groupAnagrams(strs))
strs = ["eaa","aeee"]
print(groupAnagrams(strs))
strs = ["ddddddddddg","dgggggggggg"]
print(groupAnagrams(strs))