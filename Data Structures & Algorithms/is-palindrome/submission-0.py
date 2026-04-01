class Solution:
    def isPalindrome(self, s: str) -> bool:
        izq = 0
        der = len(s) - 1

        while izq < der:

            if s[izq].isalnum() != True:
                izq += 1
                continue
            elif s[der].isalnum() != True:
                der -= 1  
                continue 

            if s[izq].lower() != s[der].lower():
                return False
            else:
                 izq += 1
                 der -= 1
        return True                 