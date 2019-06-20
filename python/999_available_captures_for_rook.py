class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        H = len(board)
        L = len(board[0])
        
        for h in range(H):
            for l in range(L):
                if board[h][l] == 'R':
                    rh = h
                    rl = l
        nums = 0
        for i in range(L-rl-1):
            if board[rh][rl+i+1] == '.':
                pass
            elif board[rh][rl+i+1] == 'B':
                break
            else:
                nums += 1
                break
        for i in range(rl):
            if board[rh][rl-1-i] == '.':
                pass
            elif board[rh][rl-i-1] == 'B':
                break
            else:
                nums += 1
                break 
        for j in range(H-rh-1):
            if board[rh+j+1][rl] == '.':
                pass
            elif board[rh+j+1][rl] == 'B':
                break
            else:
                nums += 1
                break
        for j in range(rh):
            if board[rh-1-j][rl] == '.':
                pass
            elif board[rh-1-j][rl] == 'B':
                break
            else:
                nums += 1
                break
        return nums