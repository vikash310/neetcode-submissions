# given array is not sorted
# what if given array is empty


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #nums = [1, 2, 3, 3]
        #nums_dict = {1:1, 2:1, 3:2}
        nums_dict = {}
        for i in nums:
            if i not in nums_dict.keys():
                nums_dict[i] = 1
            else:
                return True
        return False

        