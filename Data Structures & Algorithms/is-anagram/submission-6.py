from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_letters = list(s)
        list_letters_two = list(t)
        
        new_list_letters = sorted(list_letters)
        new_list_letters_two = sorted(list_letters_two)
        
        if new_list_letters == new_list_letters_two:
            return True        
        else:
            return False

s = "xx"
t = "x"
Proof = Solution()
program = Proof.isAnagram(s, t)  
print(f'is anagram {program}')   