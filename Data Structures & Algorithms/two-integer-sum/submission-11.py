class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list_index = []
        m = {}

        for i,n in enumerate(nums):
            m[n] = i

        for i,n in enumerate(nums):
            difference = target - n
            if difference in m and m[difference] != i:
                list_index.append(i)
                list_index.append(m[difference])
                return list_index
            else:
                continue
        return f"no hay"                