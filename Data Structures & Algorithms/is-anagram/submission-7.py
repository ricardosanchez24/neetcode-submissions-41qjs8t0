from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        string1_set = set(s)
        string2_set = set(t)

        counted_strin1 = len(s)
        counted_strin2 = len(t)

        counted_letters_string1 = Counter(s)
        counted_letters_string2 = Counter(t)

        if counted_letters_string1 == counted_letters_string2 and counted_strin1 == counted_strin2 and string1_set == string2_set:
            return True
        return False    