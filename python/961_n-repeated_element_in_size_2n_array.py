class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        nums = [0] * 10000
        for a in A:
            if nums[a] == 0:
                nums[a] = 1
            else:
                return a
        