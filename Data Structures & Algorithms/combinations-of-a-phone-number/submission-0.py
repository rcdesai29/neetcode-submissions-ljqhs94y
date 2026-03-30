class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: 
            return []
        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = []
        
        def dfs(i, text):
            if i >= len(digits):
                res.append("".join(text))
                return
            
            for l in phone_map[digits[i]]:
                text.append(l)
                dfs(i+1, text)
                text.pop()

        dfs(0, [])
        return res
