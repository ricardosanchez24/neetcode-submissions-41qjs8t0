class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cont = 0
        cont_max = 0
        dupli = {}
        left = 0

        for i in range(len(s)):
            if s[i] in dupli and dupli[s[i]] >= dupli[s[left]]:   
                left = dupli[s[i]] + 1
            dupli[s[i]] = i    
            
            cont = i - left + 1  
            cont_max = max(cont_max,cont)

        return cont_max