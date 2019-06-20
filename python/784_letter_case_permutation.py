class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        if not S:
            return ['']
        ans = []
        flag = 0
        for i,s in enumerate(S):
            if s.isalpha():
                flag = 1
                subans = self.letterCasePermutation(S[i+1:])
                for string in subans:
                    ans.append(S[:i]+s.lower()+string)
                    ans.append(S[:i]+s.upper()+string)
                break
        if not flag:
            ans = [S]
        return ans
        
