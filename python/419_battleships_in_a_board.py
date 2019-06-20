class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if not board:
            return 0
        self.count = 0
        H,L = len(board), len(board[0])
        
        def neigh(s,t):
            for (i,j) in [(s-1,t),(s+1,t),(s,t+1),(s,t-1)]:
                if -1<i<H and -1<j<L and board[i][j] == 'X':
                    yield i,j
        
        def dfs(i,j):
            for s,t in neigh(i,j):
                board[s][t] = self.count
                dfs(s,t)
            
            
            
        for i in range(H):
            for j in range(L):
                if board[i][j] == 'X':
                    self.count += 1
                    dfs(i,j)
        
        return self.count
    
## changed the matrix
                    
        