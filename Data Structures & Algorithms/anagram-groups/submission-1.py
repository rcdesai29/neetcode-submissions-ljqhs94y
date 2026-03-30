class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list) # {count: [cat, act]}

        for s in strs: #getting each string in the list
            count = [0] * 26 
            for c in s: #each character in the strings
                count[ord('a') - ord(c)] += 1 #update c occurence 
            hashmap[tuple(count)].append(s) #append the string for its count
        
        # print(hashmap.items())
        res = []
        for arr, s in hashmap.items():
            res.append(s)
        if res:
            return res
