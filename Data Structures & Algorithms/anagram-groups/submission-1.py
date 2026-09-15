class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            # s = "act"
            count = [0] * 26
            #count = [0,0,0,0.....,25th place]
            for c in s:
                count[ord(c)-ord("a")] += 1
            #count = [1,0,1, .....1 at place of t(ascii of t:116- ascii of 1:97 =19)]
            res[tuple(count)].append(s)
            # res = {(1,0,1.....1):["act"]}
        
        return list(res.values())




