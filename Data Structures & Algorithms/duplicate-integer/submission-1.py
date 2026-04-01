class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vistos = set()

        for n in nums:
            if n in vistos:
                return True
            else:
                vistos.add(n)    
        return False   

num_list = [1,5,6,8,45,20,2]
Proof = Solution()
program = Proof.hasDuplicate(num_list) 
print(f"the values for list is {program}")            