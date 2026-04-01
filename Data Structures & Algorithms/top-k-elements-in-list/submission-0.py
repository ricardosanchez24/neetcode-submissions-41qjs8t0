class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        list_result = []

        for num in nums:
            if num in hash_map:
                hash_map[num] += 1
                continue
            hash_map[num] = 0

        elementos_ordenados = sorted(hash_map.items(),key=lambda item:item[1],reverse=True) 
        
        elementos_ordenados_dict = dict(elementos_ordenados)

        for clave,valor in enumerate(elementos_ordenados_dict):
            if len(list_result) == k:
                break
            list_result.append(valor)

          
        return list_result