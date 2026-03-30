class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        map = {}
        maxFreq = 0
        for r in range(len(s)):
            map[s[r]] = 1 + map.get(s[r], 0)
            maxFreq = max(maxFreq, map[s[r]])
            while (r - l + 1) - maxFreq > k:
                map[s[l]] -= 1
                l += 1 
            res = max(res, r - l + 1)
        return res

