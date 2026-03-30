class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count1 = {}
        for i in range(len(s1)):
            count1[s1[i]] = 1 + count1.get(s1[i], 0)
        need = len(count1)
        for i in range(len(s2)):
            count2, cur = {}, 0
            for j in range(i, len(s2)):
                count2[s2[j]] = 1 + count2.get(s2[j], 0)

                if count1.get(s2[j], 0) == count2[s2[j]]:
                    cur += 1
                if count1.get(s2[j], 0) < count2[s2[j]]:
                    break
                if cur == need:
                    return True

        return False