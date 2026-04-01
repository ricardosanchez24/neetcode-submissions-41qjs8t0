from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resp = defaultdict(list)

        for word in strs:
            if word in resp:
                continue
            count = [0] * 26
            for l in word:
                count[ord(l) - ord('a')] += 1
            
            resp[tuple(count)].append(word)


        return list(resp.values())