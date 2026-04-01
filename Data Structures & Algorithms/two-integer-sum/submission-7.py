class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # We created the list where the indexes will go.
        list_index =[]
        # we iterate the indices
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in nums:
                index_difference = nums.index(difference)
                
                if difference != nums[i]:
                    # If they are not equal, we just add the indices to the list    
                    list_index.append(i)
                    list_index.append(index_difference)
                    return list_index
                if difference == nums[i]:
                        index_difference = nums.index(difference)
                        try:
                            second_index = nums.index(difference,index_difference+1)
                        except ValueError:
                            continue    
                        if second_index:
                            list_index.append(i)
                            list_index.append(second_index)
                            return list_index 
                        else:
                            continue           
                continue # for verify the errors   


p = Solution()
b = p.twoSum([5,5],10)       
print(b)             