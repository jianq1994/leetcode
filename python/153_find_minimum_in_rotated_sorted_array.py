class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums: return 
        l,r = 0, len(nums)-1
        while(l<r):
            m = (l+r)//2
            if nums[l] <= nums[m] < nums[r]:
                return nums[l]
            elif nums[l] > nums[m]:
                r = m
            else:
                l = m+1
        return nums[l]