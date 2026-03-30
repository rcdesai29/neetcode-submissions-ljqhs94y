class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS = {}
        countT = {}

        for i in range(len(s)):
            char = s[i]
            countS[char] = 1 + countS.get(char, 0)
            charT = t[i]
            countT[charT] = 1 + countT.get(charT, 0)
        
        for c in s:
            if countS[c] != countT.get(c, 0):
                return False
        return True
        