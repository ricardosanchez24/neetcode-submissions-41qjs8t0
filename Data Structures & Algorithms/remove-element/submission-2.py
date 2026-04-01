class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
            #tableHash = {}
            table = []

            for i,n in enumerate(nums):
                if n == val:
                    #tableHash[i] = n
                    table.append(i)

            #hash_ord = dict(sorted(tableHash.items(),key=lambda item: item[0],reverse=True))
            table.sort(reverse=True)
            for p in table:
                del nums[p] 

            k = len(nums)
            return k    