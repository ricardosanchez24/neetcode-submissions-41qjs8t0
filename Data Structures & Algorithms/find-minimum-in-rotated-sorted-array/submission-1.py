class Solution:
    def findMin(self, nums: List[int]) -> int:
        inicio = 0
        fin = len(nums) - 1
        

        while inicio <= fin:

            medio = (fin + inicio) // 2

            if nums[medio] > nums[fin]:
                inicio = medio + 1
                continue
            elif nums[medio] < nums[fin]:
                fin = medio
                continue
            else:
                return nums[fin]    
                
        return nums[medio]                  