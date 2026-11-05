class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        charset = set()

        for j in range(len(s)):
            while s[j] in charset:
                charset.remove(s[l])
                l += 1
            charset.add(s[j])
            res  = max(res, j - l + 1)

        return res


            
        