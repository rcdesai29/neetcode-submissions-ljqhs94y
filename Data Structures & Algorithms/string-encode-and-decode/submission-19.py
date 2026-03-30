class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        print(res)
        return res
    def decode(self, s: str) -> List[str]:
        result = []

        i = 0
        while i < len(s):
            string = ""
            j = i
            while s[j] != '#':
                j+=1
            length = int(s[i:j])
            string = s[j+1 : j+1+length]
            result.append(string)
            i = j+1+length
        return result