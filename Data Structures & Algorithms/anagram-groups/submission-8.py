class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #strs_len = len(strs)
        #if 1 <= strs_len <= 10000:
        # if len(strs) == 1:
        #     return [strs]
        res = defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)- ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())

            
            