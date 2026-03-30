class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        need = {}
        for c in t:
            need[c] = 1 + need.get(c, 0)
        
        required = len(need)
        meets = False
        l = 0
        window = {}
        have = 0
        res = ""
        resLen = float('infinity')
        for r in range(len(s)):
            char = s[r]
            window[char] = 1 + window.get(char, 0)

            if char in need and window[char] == need[char]:
                have +=1
           
            while have == required:
                if (r-l+1) < resLen:
                    res = [l, r]
                    print(res)
                    resLen = (r-l+1)
                meets = True
                charLeft = s[l]
                window[charLeft] -=1
                if charLeft in need:
                    if window[charLeft] < need[charLeft]:
                        have -=1
                l += 1

        if meets:
            l, r = res
        else:
            return ""
        return s[l:r+1] if resLen != float('infinity') else ""


