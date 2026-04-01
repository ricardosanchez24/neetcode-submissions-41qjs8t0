class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}

        for i, n in enumerate(nums):
            difference = target - n
            if difference in m:
                return [m[difference], i]
            m[n] = i  