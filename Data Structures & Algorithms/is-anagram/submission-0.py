class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countT, countS = {}, {}

        for c in range(len(s)):
            countS[s[c]] = 1 + countS.get(s[c], 0)
            countT[t[c]] = 1 + countT.get(t[c], 0)

        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True

