class Solution:
    memo = {}
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left,right+1):
            if i in Solution.memo:
                if Solution.memo[i]:
                    ans.append(i)
            else:
                s = str(i)
                if '0' in s:
                    Solution.memo[i] = False
                else:
                    flag = 0
                    for ss in s:
                        if i%int(ss) != 0:
                            flag = 1
                            break
                    if flag:
                        Solution.memo[i] = False
                    else:
                        Solution.memo[i] = True
                        ans.append(i)
        return ans
                
        
        