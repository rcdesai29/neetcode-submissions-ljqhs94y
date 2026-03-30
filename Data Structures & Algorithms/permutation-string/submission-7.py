class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        freq1, freq2 = {}, {}

        for i in range(len(s1)):
            freq1[s1[i]] = 1 + freq1.get(s1[i], 0)
            freq2[s2[i]] = 1 + freq2.get(s2[i], 0)
        
        matches = 0
        need = len(freq1)
        for char in freq1:
            if freq1[char] == freq2.get(char, 0):
                matches +=1
        if matches == need:
            return True
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == need:
                return True

            char_right = s2[r]
            freq2[char_right] = 1 + freq2.get(char_right, 0)

            if char_right in freq1:
                if freq1[char_right] == freq2[char_right]:
                    matches +=1
                elif freq1[char_right]+1 == freq2[char_right]:
                    matches -=1
            
            char_left = s2[l]
            freq2[char_left] -=1
            if char_left in freq1:
                if freq1[char_left] == freq2[char_left]:
                    matches +=1
                elif freq1[char_left]-1 == freq2[char_left]:
                    matches -=1
            l+=1
        return matches == need

