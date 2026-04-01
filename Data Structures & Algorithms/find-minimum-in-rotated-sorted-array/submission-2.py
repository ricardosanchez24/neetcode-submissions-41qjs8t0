class Solution:
    def findMin(self, nums: List[int]) -> int:
        inicio = 0
        fin = len(nums) - 1
        
        if len(nums) == 1:
            return nums[0]

        while inicio < fin:

            medio = (fin + inicio) // 2

            if nums[medio] > nums[fin]:
                inicio = medio + 1
                
            elif nums[medio] < nums[fin]:
                fin = medio
            '''    
            else:
                return nums[medio]
            '''        
                
        return nums[inicio]                  