class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        up,dow = len(S),0
        ans = []
        for s in S:
            if s == 'I':
                ans.append(dow)
                dow += 1
            else:
                ans.append(up)
                up -= 1
        return ans+[dow]
        