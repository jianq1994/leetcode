# from collections import stack
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        s1 = 0
        s2 = 0
        for c in moves:
            if c == 'U':
                s1 += 1
            elif c == 'D':
                s1 -= 1
            elif c == 'L':
                s2 -= 1
            else:
                s2 += 1
        if s1 == 0 and s2 == 0:
            return True
        return False
            
        