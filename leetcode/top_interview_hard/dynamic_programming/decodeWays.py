class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        dic = {"": 1, "0": 0}
        for i in range(9):
            dic[str(i+1)] = 1

        def decode(s):
            if s in dic.keys():
                return dic[s]
            if s[0] == "0":
                return 0
            if int(s[0:2]) <= 26:
                if s[1:] not in dic:
                    dic[s[1:]] = decode(s[1:])
                if s[2:] not in dic:
                    dic[s[2:]] = decode(s[2:])
                dic[s] = dic[s[1:]] + dic[s[2:]]
                # print(s + "  " + str(dic[s]))
                return dic[s]
            else:
                if s[1:] not in dic:
                    dic[s[1:]] = decode(s[1:])
                dic[s] = dic[s[1:]]
                # print(s + "  " + str(dic[s]))
                return dic[s]

        return decode(s)

        

sol = Solution()
print(sol.numDecodings("123123"))
"""
print(sol.numDecodings("226"))
print(sol.numDecodings("12"))
print(sol.numDecodings("0"))
print(sol.numDecodings("06"))
print("Fibonacci Numbers:")
print(sol.numDecodings("1"))
print(sol.numDecodings("11"))
print(sol.numDecodings("111"))
print(sol.numDecodings("1111"))
print(sol.numDecodings("11111"))
print(sol.numDecodings("111111"))
print(sol.numDecodings("1111111"))
print(sol.numDecodings("11111111111111111111111111111111"))
"""