class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # if not nums: return
        # if len(nums) == 1: return 0
        # if nums[0] > nums[1]: return 0
        # if nums[-1] > nums[-2]: return len(nums)-1
        # for i in range(1,len(nums)-1):
        #     if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
        #         return i
        
        if not nums: return
        if len(nums) == 1: return 0
        if nums[0] > nums[1]: return 0
        if nums[-1] > nums[-2]: return len(nums)-1
        l,r = 1,len(nums)-2
        while(l<r):
            m = (l+r)//2
            if(nums[m-1]>nums[m]):
                r = m
            elif(nums[m]<nums[m+1]):
                l = m+1
            else:
                return m
        return l
            