class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        res = 0
        for num in nums:
            curr = num
            if curr - 1 not in store:
                streak = 0
                while curr in store:
                    streak += 1
                    curr += 1
                res = max(res, streak)

        return res
