class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
            tableHash = {}
            lista = []

            for i,n in enumerate(nums):
                if n == val:
                    tableHash[i] = n

            for p in tableHash:
               lista.append(p)

            nueva_lista = sorted(lista,reverse=True)  

            for p in nueva_lista:
                del nums[p] 

            k = len(nums)
            return k    