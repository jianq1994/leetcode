def left(nums, target):
    l = 0 
    r = len(nums) - 1
    while(l<r):
        m = (l+r)//2
        if target == nums[m]:
            r = m
        else:
            l = m+1
    return l

def right(nums, target):
    l = 0
    r = len(nums) - 1
    while(l<r):
        m = (l+r+1)//2
        if target == nums[m]:
            l = m
        else:
            r = m-1
    return r
            

class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1,-1]
        l = 0
        r = len(nums) - 1
        while(l<=r):
            m = (l+r)//2
            if target == nums[m]:
                break
            elif target > nums[m]:
                l = m+1
            else:
                r = m-1
        if l>r:
            return [-1,-1]
        l = left(nums[:m+1], target)
        r = right(nums[m:], target)
        return [l,r+m]