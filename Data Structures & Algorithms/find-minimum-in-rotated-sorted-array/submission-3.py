class Solution:
    def findMin(self, nums: List[int]) -> int:
        inicio = 0
        fin = len(nums) - 1
        

        while inicio < fin:

            medio = (fin + inicio) // 2

            if nums[medio] > nums[fin]:
                inicio = medio + 1
                
            elif nums[medio] < nums[fin]:
                fin = medio
            
                
        return nums[inicio]                  