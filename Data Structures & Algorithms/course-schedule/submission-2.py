class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = {i: [] for i in range(numCourses)} 
        visit = set()
        for crse, prereq in prerequisites:
            courses[crse].append(prereq)
        
        def dfs(crse):
            if crse in visit:
                return False

            if courses[crse] == []:
                return True
            
            visit.add(crse)
            for prereq in courses[crse]:
                if not dfs(prereq):
                    return False
            visit.remove(crse)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True