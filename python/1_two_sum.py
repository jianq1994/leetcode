class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """    
        seen = {}
        for i,num in enumerate(nums):
            if target-num in seen:
                return [seen[target-num],i]
            else:
                seen[num] = i
        