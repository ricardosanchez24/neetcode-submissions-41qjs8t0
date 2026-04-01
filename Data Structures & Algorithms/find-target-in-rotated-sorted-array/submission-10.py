class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            medio = (r + l) // 2

            if nums[medio] == target:
                return medio
            
            if nums[l] <= nums[medio]:
                if target >= nums[l] and target < nums[medio]:
                    r = medio - 1
                else:
                    l = medio + 1    
                   
            else:
                if target > nums[medio] and target <= nums[r]:
                    l = medio + 1   
                else:
                    r = medio - 1                
            

        return -1        
