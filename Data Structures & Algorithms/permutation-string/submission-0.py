from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        obj = Counter(s1)
        
        for i in range(len(s2) - k+1):

            window = Counter(s2[i: i + k])
            
            if obj == window:
                return True

        return False        