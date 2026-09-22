class Graph:
    
    def __init__(self):
        self.adj = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adj:
            self.adj[src] = set()
        if dst not in self.adj:
            self.adj[dst] = set()
        self.adj[src].add(dst)
        

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adj:
            return False
        for value in self.adj[src]:
            if value == dst:
                self.adj[src].remove(value)
                return True
        return False

    def hasPath(self, src: int, dst: int) -> bool:
        if src == dst:
            return True
        visited = set()

        for nei in self.adj[src]:
            if nei == dst:
                return True
            if self.dfs(visited, nei, dst):
                return True
        return False

    def dfs(self, visited, src, dst):
        if src in visited:
            return False
        visited.add(src)
        for nei in self.adj[src]:
            if nei == dst:
                return True
            if self.dfs(visited, nei, dst):
                return True
        return False
        
