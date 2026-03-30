class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count1 = {}
        for c in s1:
            count1[c] = 1 + count1.get(c, 0)
        
        count2 = {}
        for i in range(len(s1)):
            count2[s2[i]] = 1 + count2.get(s2[i], 0)
        if count2 == count1:
            return True    
        
        for j in range(len(s1), len(s2)):
            count2[s2[j]] = 1 + count2.get(s2[j], 0)
            count2[s2[j-len(s1)]] -= 1
            if count2[s2[j-len(s1)]] == 0:
                del count2[s2[j-len(s1)]]
            if count2 == count1:
                return True 
        return False
