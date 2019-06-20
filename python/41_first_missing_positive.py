class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 1
        for i,num in enumerate(nums):
            while(1):
                if num > len(nums) or num <= 0 or nums[num-1] == num:
                    break
                else:
                    tmp = nums[num-1]
                    nums[num-1] = num
                    num = tmp
        for i,num in enumerate(nums):
            if num != i+1:
                return i+1
        return len(nums)+1