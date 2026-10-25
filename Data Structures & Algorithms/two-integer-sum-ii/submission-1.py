class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        diff = {}
        n = len(numbers)
        if n >= 2:
            for i in range(n):
                sec_num = target - numbers[i]
                if sec_num in diff:
                    return [diff[sec_num]+1, i +1]
                diff[numbers[i]] = i
        return []
