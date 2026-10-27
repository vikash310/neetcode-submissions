class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first_index = [-1]*26
        res = -1
        for i, c in enumerate(s):
            j = ord(c) - ord("a") 
            if first_index[j] != -1:
                res = max(res, i - first_index[j]-1)
            else:
                first_index[j]= i

        return res
