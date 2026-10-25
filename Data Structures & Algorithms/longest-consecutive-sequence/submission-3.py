class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        res = 0
        for num in store:
            curr = num
            streak = 0

            if curr -1 not in store:
                while curr in store:
                    streak += 1
                    curr += 1

            res = max(res, streak)
        return res
