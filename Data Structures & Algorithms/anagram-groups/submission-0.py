from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for word in strs:
            cont = [0] * 26
            for letter in word:
                cont[ord(letter) - ord('a')] += 1

            res[tuple(cont)].append(word)

        return list(res.values())