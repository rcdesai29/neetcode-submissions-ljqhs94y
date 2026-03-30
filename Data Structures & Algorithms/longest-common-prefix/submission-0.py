class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        
        for i in range(1, len(strs)):
            s = strs[i]
            if len(prefix) > len(s):
                prefix,s = s, prefix

            j = 0
            while j < len(prefix) and s[j] == prefix[j]:
                j += 1
            prefix = prefix[:j]
        return prefix


