class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_length = len(nums)
        if num_length >= 2:
            diff = {}
            for i in range(0, num_length):
                target_diff = target - nums[i]
                if target_diff in diff:
                    return [diff[target_diff], i]
                diff[nums[i]] = i

