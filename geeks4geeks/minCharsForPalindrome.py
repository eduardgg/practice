
class Solution:
    
    # Python program for getting minimum character to be
    # added at front to make string palindrome

    def computeLPSArray(self, pat):
        n = len(pat)
        lps = [0] * n

        # lps[0] is always 0
        len_lps = 0

        # loop calculates lps[i] for i = 1 to n-1
        i = 1
        while i < n:
        
            # If the characters match, increment len
            # and set lps[i]
            if pat[i] == pat[len_lps]:
                len_lps += 1
                lps[i] = len_lps
                i += 1
            
            # If there is a mismatch
            else:
            
                # If len is not zero, update len to 
                # the last known prefix length
                if len_lps != 0:
                    len_lps = lps[len_lps - 1]
                    
                # No prefix matches, set lps[i] to 0
                else:
                    lps[i] = 0
                    i += 1
        return lps

    # Method returns minimum character to be added at
    # front to make string palindrome
    def minChar(self, s):

        # Get concatenation of string, special character
        # and reverse string
        s = s + "$" + s[::-1]

        # Get LPS array of this concatenated string
        lps = self.computeLPSArray(s)

        # By subtracting last entry of lps array from
        # string length, we will get our result
        return len(s) - lps[-1]



if __name__ == "__main__":
    for _ in range(int(input())):
        s = input()
        obj = Solution()
        ans = obj.minChar(s)
        print(ans)
        print("~")