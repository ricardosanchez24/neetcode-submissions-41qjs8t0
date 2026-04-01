class Solution:
    def search(self, nums: List[int], target: int) -> int:
        hash_set = set(nums)
        l = 0
        r = len(nums) - 1

        if not target in hash_set:
            return -1
        if len(nums) == 1 and target == nums[0]:
            return 0 

        if len(nums) == 2:
            for i in range(len(nums)):
                if nums[i] == target:
                    return i    

        while l < r:
            medio = (r + l) // 2

            if nums[medio] == target:
                return medio
            elif nums[r] == target:
                return r
            elif nums[l] == target:
                return l        

            if nums[medio] > nums[r] and nums[medio] > target:
                l = medio
                if nums[medio - 1] == target:
                    return medio - 1

            if nums[medio] < nums[r] and nums[medio] > target:
                r = medio

            if nums[medio] < nums[r] and nums[medio] < target:
                r = medio - 1
            
            if nums[medio] > nums[r] and nums[medio] < target:
                l =  medio + 1    

               

        return medio        
