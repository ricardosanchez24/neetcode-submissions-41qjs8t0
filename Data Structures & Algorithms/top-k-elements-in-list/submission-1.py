import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        list_result = []

        for num in nums:        #0(n)
            if num in hash_map:
                hash_map[num] += 1
                continue
            hash_map[num] = 1

        resultado = heapq.nlargest(k,hash_map.keys(),key=hash_map.get)    
        
        return resultado