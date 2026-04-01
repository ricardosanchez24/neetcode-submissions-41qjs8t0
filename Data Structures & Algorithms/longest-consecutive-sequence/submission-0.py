class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_secuencia = 0
        for n in nums:
            if n - 1 not in nums_set:
                secuencia = 1
                condicion_while = True
                while condicion_while:
                    if n + secuencia in nums_set:  
                        secuencia += 1
                        continue
                    else:
                        condicion_while = False    
                max_secuencia = max(max_secuencia,secuencia)
            else:
                continue   
        return max_secuencia           