class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i,n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue

            izq = i + 1
            der = len(nums) - 1
            while izq < der:
                suma = n + nums[izq] + nums[der]

                if suma > 0:
                    der -= 1
                elif suma < 0:
                    izq += 1
                else:
                    res.append([n, nums[izq], nums[der]])
                    izq += 1
                    while nums[izq] == nums[izq - 1] and izq < der:
                        izq += 1
        return res                           