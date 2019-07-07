class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums) <= 1: return
        f = s = 0
        while(1):
            f = nums[f]
            s = nums[nums[s]]
            if s == f:
                break
        f = 0
        while(1):
            f = nums[f]
            s = nums[s]
            if s == f:
                return s
            
            
        # s = set([])
        # for i in nums:
        #     if i in s:
        #         return i
        #     else:
        #         s.add(i)