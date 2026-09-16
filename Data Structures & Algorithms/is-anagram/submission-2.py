class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            s_dict ={}
            for key in s:
                s_dict[key] = s_dict.get(key,0)+1
            for key in t:
                s_dict[key] = s_dict.get(key,0) - 1
                if s_dict[key] == -1:
                    return False
            if sum(s_dict.values()) == 0:
                return True
        return False
                
        