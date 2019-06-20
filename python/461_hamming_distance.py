class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        ans = 0
        if not x and not y:
            return 0
        if x%2 != y%2:
            ans += 1
        return ans+self.hammingDistance(x//2,y//2)
        