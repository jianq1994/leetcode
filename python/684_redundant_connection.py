class DSU():
    def __init__(self):
        self.par = list(range(10001))
    def parent(self,x):
        if self.par[x] != x:
            return self.parent(self.par[x])
        return self.par[x]
    def union(self,x,y):
        self.par[self.parent(x)] = self.par[self.parent(y)]

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU()
        for edge in edges:
            if dsu.parent(edge[0]) == dsu.parent(edge[1]):
                return edge
            else:
                dsu.union(*edge)