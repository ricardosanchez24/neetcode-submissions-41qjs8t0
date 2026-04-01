class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        return res    
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            longitud = int(s[i:j])
            res.append(str(s[j + 1: j + 1 + longitud]))
            i = j + 1 + longitud
        return res        