class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
            tableHash = {}
            

            for i,n in enumerate(nums):
                if n == val:
                    tableHash[i] = n
                    
            hash_ord = dict(sorted(tableHash.items(),key=lambda item: item[0],reverse=True))
            
            for p in hash_ord:
                del nums[p] 

            k = len(nums)
            return k