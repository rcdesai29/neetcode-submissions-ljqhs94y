class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        r = 0
        dupes = {}
        res = 0
        while r < len(s):
            if s[r] in dupes:
                l = max(dupes[s[r]] + 1, l)
            dupes[s[r]] = r
            res = max(res, r - l+1)
            r += 1
        return res