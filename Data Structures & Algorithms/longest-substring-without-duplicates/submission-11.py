class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = {}
        l = 0
        r = 0
        res = 0

        while r < len(s):
            if s[r] in count:
                l = max(l, count[s[r]] + 1)
            count[s[r]] = r
            res = max(res, r - l + 1)
            r += 1
        return res