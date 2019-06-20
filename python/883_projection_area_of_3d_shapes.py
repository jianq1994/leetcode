class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        H, L = len(grid), len(grid[0])
        Left, Down = [0]*H, [0]*L
        Sur = 0
        for i in range(H):
            for j in range(L):
                Left[i] = max(Left[i],grid[i][j])
                Down[j] = max(Down[j],grid[i][j])
                if grid[i][j] != 0:
                    Sur += 1
        return sum(Left)+sum(Down)+Sur
        