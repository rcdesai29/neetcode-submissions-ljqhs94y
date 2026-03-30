class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        keyPad = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : 'wxyz'
        }

        res = []

        def dfs(i, temp):
           
            if len(temp) == len(digits):
                res.append("".join(temp))
                return
            
            for alph in keyPad[digits[i]]:
                temp.append(alph)
                dfs(i+1, temp)
                temp.pop()



        dfs(0, [])
        return res