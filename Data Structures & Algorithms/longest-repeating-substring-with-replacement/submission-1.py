class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cont = {}
        res = 0
        l = 0
        maxf = 0

        for r in range(len(s)):
            cont[s[r]] = 1 + cont.get(s[r],0)
            maxf = max(maxf,cont[s[r]])

            if (r - l + 1) - maxf > k:
                cont[s[l]] -= 1
                l += 1
            res = max(res,(r - l + 1))

        return res        