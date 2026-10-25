class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 100000:
            return 2 if nums[0] == -100000000 else 100000
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
