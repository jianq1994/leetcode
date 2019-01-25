#100%
class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 3:
            return sum(nums)
        nums.sort()
        diff = float('Inf')
        closest = float('Inf')
        for i in range(len(nums)):
            j = i+1
            k = len(nums)-1
            while(j<k):
                csum = int(nums[i] + nums[j] + nums[k])
                if target == csum:
                    return target
                if diff > abs(csum-target):
                    closest = csum
                    diff = abs(csum-target)
                if csum > target:
                    k -= 1
                else:
                    j += 1
        return int(closest)
                
        