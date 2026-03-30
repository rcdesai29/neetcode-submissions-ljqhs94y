class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:    
            res += str(len(s) )+ "#" + s
        return res
    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1

            lenght = int(s[i:j])
            """
                5#hello5#world
                i = 5, j = #
            """
            j += 1
            res.append(s[j: j + lenght])
            i = j + lenght
            print(i)
        return res

