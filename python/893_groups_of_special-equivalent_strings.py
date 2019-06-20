from collections import Counter
class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        def count(A):
            ans = []
            for a in A:
                t = [0]*52
                for num,aa in enumerate(a):
                    t[ord(aa)-ord('a')+26*(num%2)] += 1
                ans.append(tuple(t))
            return ans
        
        return len(set(count(A)))
            