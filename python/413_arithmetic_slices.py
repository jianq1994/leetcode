class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0 
        
        dif = A[1] - A[0]
        count = 0
        ans = 0
        
        for i in range(len(A)-2):
            if A[i+2] - A[i+1] == dif:
                count += 1
                ans += count
            else:
                dif = A[i+2] - A[i+1]
                count = 0
        return ans
                
                
            