class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        myset = set()

        for i in range(len(nums)):

            if not nums[i] in myset:
                myset.add(nums[i])
            else:
                return nums[i]

        return None            