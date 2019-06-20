class DSU():
    def __init__(self, L):
        self.parent = {}
        for i in range(L+1):
            for j in range(L+1):
                self.parent[(i,j)] = (i,j)
        for k in range(L+1):
            self.parent[k,L] = (0,0)
            self.parent[k,0] = (0,0)
            self.parent[0,k] = (0,0)
            self.parent[L,k] = (0,0)
    def par(self, x):
        if self.parent[x] != x:
            return self.par(self.parent[x])
        return x
    def union(self,x,y):
        self.parent[self.par(x)] = self.parent[self.par(y)]

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        if not grid:
            return 0
        ans = 1
        L = len(grid)
        dsu = DSU(L)
        for numi,line in enumerate(grid):
            for numj,c in enumerate(line):
                if c == '/':
                    if dsu.par((numi,numj+1))== dsu.par((numi+1,numj)):
                        ans += 1
                        dsu.union((numi,numj+1),(numi+1,numj))
                    else:
                        dsu.union((numi,numj+1),(numi+1,numj))
                if c == '\\':
                    if dsu.par((numi+1,numj+1)) == dsu.par((numi,numj)):
                        ans += 1
                        dsu.union((numi+1,numj+1),(numi,numj))
                    else:
                        dsu.union((numi+1,numj+1),(numi,numj))
        return ans
                