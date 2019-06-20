import math
class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:

        ans = 0
        for i in range(L,R+1):
            num = sum([int(j) for j in str(bin(i)[2:])])
            flag = 0
            for k in range(2,int(math.sqrt(num))+2):
                if num % k ==0 and num != k:
                    flag = 1
                    break
            if not flag and num != 1:
                ans += 1
        return ans
                
        
        
#         memo = []
        
#         def countWithMemo(L,R):
#             if R < len(memo):
#                 return sum(memo[L:R+1])
            
#             for i in range(len(memo),R+1):
#                 num = sum([int(j) for j in str(bin(i)[2:])])
#                 flag = 0
#                 for k in range(2,int(math.sqrt(num))+2):
#                     if num % k ==0:
#                         flag = 1
#                         break
#                 if not flag:
#                     memo.append(1)
#                 else:
#                     memo.append(0)
            
#             return sum(memo[L:R+1])
        
#         return countWithMemo(L,R)