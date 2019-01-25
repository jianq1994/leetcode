class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        l = 0
        r = len(nums)-1
        while(l<=r):
            m = (l+r)//2
            if nums[m] == target:
                return m
            if nums[l] <= nums[m]:
                if nums[m] < target or nums[l] > target:
                    l = m+1
                else:
                    r = m-1
            else:
                if nums[m] < target and nums[l] > target:
                    l = m+1
                else:
                    r = m-1
        return -1