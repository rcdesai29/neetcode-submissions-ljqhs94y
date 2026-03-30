class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {i: [] for i in range(numCourses)}
        for crse, pre in prerequisites:
            prereq[crse].append(pre)
        
        visit, cycle = set(),set()
        res = []
        def dfs(node):
            if node in visit:
                return True
            if node in cycle:
                return False
            
            cycle.add(node)
            for nei in prereq[node]:
                if not dfs(nei):
                    return False
                
            cycle.remove(node)
            visit.add(node)
            res.append(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return res